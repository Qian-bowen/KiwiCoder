#include "connector.h"
#include "kiwi/include/constants.h"
#include "kiwi/include/file.h"
#include <unistd.h>
#include <fcntl.h>

// AbstractServerConnector

AbstractServerConnector::AbstractServerConnector(int thread_num):thread_pool(thread_num),thread_num(thread_num),is_running(false){

}

AbstractServerConnector::~AbstractServerConnector(){
    this->StartListening();
}

bool AbstractServerConnector::StartListening(){
    if(this->is_running){
        return false;
    }
    if(!this->InitializeListener()){
        return false;
    }
    this->is_running=true;
    this->listener_thread=std::unique_ptr<std::thread>(new std::thread(&AbstractServerConnector::ListenLoop,this));
    return true;
}

bool AbstractServerConnector::StopListening(){
    if (!this->is_running){
        return false;
    }

    this->is_running = false;
    this->listener_thread->join();
    return true;
}

void AbstractServerConnector::ListenLoop(){
    while(this->is_running){
        int fd=this->GetFrontConnection();
        if(fd<0){
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            continue;
        }
        if(this->thread_num>0){
            this->thread_pool.enqueue(&AbstractServerConnector::HandleConnection,this,fd);
        }else{
            this->HandleConnection(fd);
        }
    }
}

void AbstractServerConnector::HandleRequest(const std::string &request,std::string &response){
    this->handler->HandlerRequest(request,response);
}

void AbstractServerConnector::SetHandler(std::shared_ptr<IProtocolHandler> handler){
    this->handler=handler;
}


// TcpSocketConnector

TcpSocketConnector::TcpSocketConnector(const std::string &ip, const unsigned int &port,int thread_num)
    :AbstractServerConnector(thread_num),ip(ip),port(port){
}

TcpSocketConnector::~TcpSocketConnector(){
    shutdown(this->socket_fd, 2);
    close(this->socket_fd);
}

bool TcpSocketConnector::InitializeListener(){
    int fd;
    int opt=1;
    if((fd=socket(AF_INET,SOCK_STREAM,0))<0){
        return false;
    }
    this->socket_fd=fd;

    // set socket forcefully
    if (setsockopt(fd, SOL_SOCKET,SO_REUSEADDR|SO_REUSEPORT, &opt,sizeof(opt))) {
        return false;
    }

    // set address
    memset(&(this->address), 0, sizeof(struct sockaddr_in));
    this->address.sin_family = AF_INET;
    inet_aton(this->ip.c_str(), &(this->address.sin_addr));
    this->address.sin_port = htons(this->port);

    if(bind(fd,reinterpret_cast<struct sockaddr *>(&(this->address)), sizeof(struct sockaddr_in))!=0){
        return false;
    }

    if(listen(fd,DEFAULT_BACKLOG_CONN_SIZE)!=0){
        return false;
    }

    return true;
}

int TcpSocketConnector::GetFrontConnection(){
    struct sockaddr_in client_address;
    memset(&client_address, 0, sizeof(struct sockaddr_in));
    socklen_t address_length = sizeof(client_address);
    return accept(this->socket_fd, reinterpret_cast<struct sockaddr *>(&(client_address)), &address_length);
}

void TcpSocketConnector::HandleConnection(int connection){
    StreamReader reader(DEFAULT_BUFFER_SIZE);
    std::string request,response;
    reader.Read(request,connection,DEFAULT_DELIMITER_CHAR);
    this->HandleRequest(request,response);
    response.append(1,DEFAULT_DELIMITER_CHAR);

    StreamWriter writer;
    writer.Write(response,connection);
    close(connection);
}
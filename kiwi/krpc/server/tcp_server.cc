#include "tcp_server.h"
#include "kiwi/include/constants.h"
#include "kiwi/include/file.h"
#include <unistd.h>
#include <fcntl.h>

TcpSocketServer::TcpSocketServer(const std::string &ip, const unsigned int &port,int thread_num)
    :BaseServer(thread_num),ip(ip),port(port){
}

TcpSocketServer::~TcpSocketServer(){
    shutdown(this->socket_fd, 2);
    close(this->socket_fd);
}

bool TcpSocketServer::InitializeListener(){
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

int TcpSocketServer::GetFrontConnection(){
    struct sockaddr_in client_address;
    memset(&client_address, 0, sizeof(struct sockaddr_in));
    socklen_t address_length = sizeof(client_address);
    return accept(this->socket_fd, reinterpret_cast<struct sockaddr *>(&(client_address)), &address_length);
}

void TcpSocketServer::HandleConnection(int connection){
    StreamReader reader(DEFAULT_BUFFER_SIZE);
    std::string request,response;
    reader.Read(request,connection,DEFAULT_DELIMITER_CHAR);
    this->HandleRequest(request,response);
    response.append(1,DEFAULT_DELIMITER_CHAR);

    StreamWriter writer;
    writer.Write(response,connection);
    close(connection);
}
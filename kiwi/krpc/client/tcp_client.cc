#include "tcp_client.h"

#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#include <fcntl.h>

#include "kiwi/include/exception.h"
#include "kiwi/include/file.h"
#include "kiwi/include/constants.h"

TcpSocketClient::TcpSocketClient(const std::string &host,const unsigned int &port){

}

TcpSocketClient::~TcpSocketClient(){

}

void TcpSocketClient::SendMessage(const std::string &message, std::string &result){
    int fd=this->Connect();
    StreamWriter writer;
    std::string send_msg=message+DEFAULT_DELIMITER_CHAR;
    if(!writer.Write(send_msg,fd)){
        throw KiwiException(Errors::ERROR_RPC_CLIENT_CONNECT);
    }

    StreamReader reader(DEFAULT_BUFFER_SIZE);
    if(!reader.Read(result,fd,DEFAULT_DELIMITER_CHAR)){
        throw KiwiException(Errors::ERROR_RPC_CLIENT_CONNECT);
    }
    close(fd);
}

bool TcpSocketClient::Connect(){
    int fd;
    if((fd=socket(AF_INET,SOCK_STREAM,0))<0){
        return false;
    }

    sockaddr_in address;
    memset(&address, 0, sizeof(sockaddr_in));
    address.sin_family = AF_INET;
    inet_aton(this->host.c_str(), &(address.sin_addr));
    address.sin_port = htons(port);

    if (connect(fd,reinterpret_cast<struct sockaddr *>(&address), sizeof(struct sockaddr_in)) != 0) {
        close(fd);
        throw KiwiException(Errors::ERROR_RPC_CLIENT_CONNECT);
        return false;
    }
    return true;
}
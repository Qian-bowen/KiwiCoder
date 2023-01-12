#ifndef KRPC_TCPSERVER_H
#define KRPC_TCPSERVER_H

#include "base_server.h"
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

class TcpSocketServer:public BaseServer{
public:
    explicit TcpSocketServer(const std::string &ip, const unsigned int &port,int thread_num);
    virtual ~TcpSocketServer();

    virtual bool StartListening();
    virtual bool StopListening();

    virtual bool InitializeListener()override;
    virtual int GetFrontConnection()override;
    virtual void HandleConnection(int connection)override;

private:
    std::string ip;
    unsigned int port;
    int socket_fd;
    struct sockaddr_in address;

};

#endif
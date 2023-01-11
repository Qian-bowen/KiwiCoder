#ifndef KRPC_SERVER_CONNECTOR_H
#define KRPC_SERVER_CONNECTOR_H

#include "client_connector_handler.h"
#include "kiwi/include/thread_pool.h"

#include<string>
#include<memory>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

class AbstractServerConnector{
public:
    explicit AbstractServerConnector(int thread_num);
    virtual ~AbstractServerConnector();

    virtual bool StartListening()=0;
    virtual bool StopListening()=0;

    virtual bool InitializeListener() = 0;
    virtual int GetFrontConnection()=0;
    virtual void HandleConnection(int connection)=0;

    void HandleRequest(const std::string &request,std::string &response);
    void SetHandler(std::shared_ptr<IProtocolHandler> handler);

private:
    void ListenLoop();

private:
    std::shared_ptr<IProtocolHandler> handler;
    std::unique_ptr<std::thread> listener_thread;
    ThreadPool thread_pool;
    int thread_num;
    bool is_running;
};

class TcpSocketConnector:public AbstractServerConnector{
public:
    explicit TcpSocketConnector(const std::string &ip, const unsigned int &port,int thread_num);
    virtual ~TcpSocketConnector();

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
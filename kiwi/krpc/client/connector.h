#ifndef KRPC_CLIENT_CONNECTOR_H
#define KRPC_CLIENT_CONNECTOR_H

#include<string>

class ClientConnector{
    public:
    explicit ClientConnector();
    virtual ~ClientConnector(){}

    virtual void SendMessage(const std::string &message, std::string &result) = 0;
};

class TcpSocketClient: public ClientConnector{
public:
    explicit TcpSocketClient(const std::string &host,const unsigned int &port);
    virtual ~TcpSocketClient();

    virtual void SendMessage(const std::string &message, std::string &result)override;
private:
    std::string host;
    unsigned int port;
    int Connect();
};


#endif
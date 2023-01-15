#ifndef KRPC_TCP_CLIENT_H
#define KRPC_TCP_CLIENT_H

#include "base_client.h"

class TcpSocketClient: public BaseClient{
public:
    explicit TcpSocketClient(const std::string &host,const unsigned int &port);
    virtual ~TcpSocketClient();

    virtual void SendMessage(const std::string &message, std::string &result)override;
private:
    std::string host;
    unsigned int port;
    bool Connect();
};

#endif
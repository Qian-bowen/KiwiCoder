#ifndef KRPC_SERVER_CONNECTOR_H
#define KRPC_SERVER_CONNECTOR_H

#include "client_connector_handler.h"

#include<string>
#include<memory>

class AbstractServerConnector{
public:
    explicit AbstractServerConnector();
    virtual ~AbstractServerConnector();

    virtual bool StartListening()=0;
    virtual bool StopListening()=0;

    void HandleRequest(const std::string &request,std::string &response);
    void SetHandler(std::shared_ptr<IClientConnectHandler> handler);

private:
    std::shared_ptr<IClientConnectHandler> handler;
};

#endif
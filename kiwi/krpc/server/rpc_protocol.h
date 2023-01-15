#ifndef KRPC_SERVER_RPC_PROTOCOL_H
#define KRPC_SERVER_RPC_PROTOCOL_H

#include "protocol.h"

class RPCProtocolHandler:public BaseProtocolHandler{
public:
    RPCProtocolHandler(InvokeHandler &handler);
    virtual ~RPCProtocolHandler(){};

    
    virtual void HandleJsonRequest(const json &request,json& response) override;
    virtual bool ValidateRequestField(const json &request) override;

    virtual void WrapResult(const json& resquest,json &response, json &ret) override;
    virtual void WrapError(const json& resquest,int code,const std::string &message, json &ret) override;
    virtual void WrapException(const json& resquest,const KiwiException &exception, json &ret) override;

};


#endif
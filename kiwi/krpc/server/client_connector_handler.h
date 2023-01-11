#ifndef KRPC_CLIENT_CONNECTOR_HANDLER_H
#define KRPC_CLIENT_CONNECTOR_HANDLER_H

#include "kiwi/include/procedure.h"


class IProtocolHandler{
public:
    IProtocolHandler()=default;
    virtual ~IProtocolHandler()=default;

    virtual void HandlerRequest(const std::string &request, std::string &result) = 0;
    virtual void AddProcedure(const Procedure &procedure)=0;
};

class RPCProtocolHandler:public IProtocolHandler{

};

#endif
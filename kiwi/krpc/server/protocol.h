#ifndef KRPC_SERVER_PROTOCOL_H
#define KRPC_SERVER_PROTOCOL_H

#include "kiwi/include/procedure.h"
#include "kiwi/include/exception.h"
#include "invoke_handler.h"


class BaseProtocolHandler{
public:
    BaseProtocolHandler(InvokeHandler &handler);
    virtual ~BaseProtocolHandler();

    void HandleRequest(const std::string &request, std::string &result);
    void AddProcedure(const Procedure &procedure);

    virtual void HandleJsonRequest(const json &request,json& response) = 0;
    virtual bool ValidateRequestField(const json &request) = 0;

    virtual void WrapResult(const json& resquest,json &response, json &ret) = 0;
    virtual void WrapError(const json& resquest,int code,const std::string &message, json &ret) = 0;
    virtual void WrapException(const json& resquest,const KiwiException &exception, json &ret) = 0;

protected:
    InvokeHandler &handler;
    std::map<std::string,Procedure> procedures;

    void ProcessHandleRequest(const json &request,json& response);
    int ValidateRequest(const json &request);
};

#endif
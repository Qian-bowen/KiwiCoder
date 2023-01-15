#include "protocol.h"
#include "kiwi/include/error.h"
#include "kiwi/include/constants.h"
#include<sstream>

BaseProtocolHandler::BaseProtocolHandler(InvokeHandler &handler):handler(handler){

}

BaseProtocolHandler::~BaseProtocolHandler(){

}

void BaseProtocolHandler::HandleRequest(const std::string &request, std::string &result){
    json resp,req;
    try{
        req=json::parse(request);
        this->HandleJsonRequest(req,resp);
    }catch(const json::exception){
        this->WrapError(req,Errors::ERROR_RPC_JSON_PARSE_ERROR,Errors::ErrorMsg(Errors::ERROR_RPC_JSON_PARSE_ERROR),resp);
    }
    result = resp.dump();
}

void BaseProtocolHandler::AddProcedure(const Procedure &procedure){
    this->procedures[procedure.GetProcedureName()]=procedure;
}

void BaseProtocolHandler::ProcessHandleRequest(const json &request,json& response){
    // TODO: handler common wrapper, e.g rpc type
    Procedure &method = this->procedures[request["method"].get<std::string>()];
    if(method.GetProcedureType()==RPC_METHOD){
        this->handler.HandleMethodCall(method,request[RPC_KEY_REQUEST_METHODNAME],response);
    }else{
        this->handler.HandleNotificationCall(method,request[RPC_KEY_REQUEST_METHODNAME]);
    }
}

int BaseProtocolHandler::ValidateRequest(const json &request){
    // TODO: Validate commom wrapper
    return Errors::ERROR_NOT_EXIST;
}
#include "protocol.h"
#include "kiwi/include/error.h"
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

void BaseProtocolHandler::HandleRequestWrap(const json &request,json& response){
    // handler common wrapper, e.g rpc type
}

void BaseProtocolHandler::ValidateRequestWrap(const json &request){
    // Validate commom wrapper
}
#include "rpc_protocol.h"

RPCProtocolHandler::RPCProtocolHandler(InvokeHandler &handler):BaseProtocolHandler(handler){

}

RPCProtocolHandler::~RPCProtocolHandler(){}

void RPCProtocolHandler::HandleJsonRequest(const json &request,json& response){
    int err = this->ValidateRequest(request);
    if(err!=Errors::ERROR_NOT_EXIST){
        this->WrapError(request,Errors::ERROR_RPC_INVALID_REQUEST,Errors::ErrorMsg(Errors::ERROR_RPC_INVALID_REQUEST),response);
        return;
    }
    try{
        // call the method
        this->ProcessHandleRequest(request,response);
    }catch(const KiwiException &exception){
        this->WrapException(request,exception,response);
        return;
    }
}

bool RPCProtocolHandler::ValidateRequestField(const json &request){
    // TODO: finish according to schema
    return true;
}

void RPCProtocolHandler::WrapResult(const json& resquest,json &response, json &ret){
    // TODO: finish according to schema
}

void RPCProtocolHandler::WrapError(const json& resquest,int code,const std::string &message, json &ret){
    // TODO: finish according to schema
}

void RPCProtocolHandler::WrapException(const json& resquest,const KiwiException &exception, json &ret){
    // TODO: finish according to schema
}
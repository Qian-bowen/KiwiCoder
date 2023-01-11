# include "client.h"

Client::Client(ClientConnector &connector):connector(connector),protocol(new RpcClientProtocol()){

}

Client::~Client(){

}

void Client::CallMethod(const std::string &method, const json &params, json &result){
    std::string request,response;
    protocol->BuildRequest(method,params,request);
    connector.SendMessage(request,response);
    protocol->HandleResponse(response,result);
}

void Client::CallNotification(const std::string &method, const json &params){
    std::string request,response;
    protocol->BuildRequest(method,params,request);
    connector.SendMessage(request,response);
}
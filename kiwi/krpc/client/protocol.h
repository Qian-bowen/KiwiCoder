#ifndef KRPC_PROTOCOL_H
#define KRPC_PROTOCOL_H

#include<string>
#include<nlohmann/json.hpp>

using json = nlohmann::json;

class RpcClientProtocol{
public:
    explicit RpcClientProtocol();
    void BuildRequest(const std::string& method,const json& param,std::string &result);
    void HandleResponse(const json& response,json& result);
};

#endif
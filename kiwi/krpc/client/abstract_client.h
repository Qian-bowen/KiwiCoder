#ifndef KRPC_CLIENT_H
#define KRPC_CLIENT_H

#include "connector.h"
#include "protocol.h"

#include<string>
#include<memory>
#include<nlohmann/json.hpp>


class Client {
public:
    explicit Client(ClientConnector &connector);
    virtual ~Client();

    void CallMethod(const std::string &method, const json &params, json &result);
    void CallNotification(const std::string &method, const json &params);

private:
    ClientConnector &connector;
    std::unique_ptr<RpcClientProtocol> protocol;
};

#endif
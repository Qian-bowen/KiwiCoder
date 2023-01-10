#ifndef KRPC_CLIENT_H
#define KRPC_CLIENT_H

#include<string>
#include<nlohmann/json.hpp>

class Client {
public:
    void CallMethod(const std::string &name);
    void CallNotification(const std::string &name);

};

#endif
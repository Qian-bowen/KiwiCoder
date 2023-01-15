#ifndef KRPC_BASE_CLIENT_H
#define KRPC_BASE_CLIENT_H

#include<string>

class BaseClient{
public:
    explicit BaseClient();
    virtual ~BaseClient(){}

    virtual void SendMessage(const std::string &message, std::string &result) = 0;
};


#endif
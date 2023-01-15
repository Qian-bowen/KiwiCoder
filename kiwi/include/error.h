#ifndef Kiwi_ERROR_H
#define Kiwi_ERROR_H

#include<string>
#include<map>

class Errors{
public:
    static std::string ErrorMsg(int error_code);
    static class _init{
    public:
        _init();
    }_initializer;
private:
    static std::map<int,std::string> error_msgs;

public:
    // common error code
    static const int ERROR_NOT_EXIST;
    // error code for krpc
    static const int ERROR_RPC_JSON_PARSE_ERROR;
    static const int ERROR_RPC_METHOD_NOT_FOUND;
    static const int ERROR_RPC_INVALID_REQUEST;
    static const int ERROR_RPC_INVALID_PARAMS;
    static const int ERROR_RPC_INTERNAL_ERROR;
    static const int ERROR_RPC_CLIENT_CONNECT;

};

#endif
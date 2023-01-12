#include "kiwi/include/error.h"

Errors::_init Errors::_initializer;

const int Errors::ERROR_RPC_JSON_PARSE_ERROR=-1001;
const int Errors::ERROR_RPC_METHOD_NOT_FOUND=-1002;
const int Errors::ERROR_RPC_INVALID_REQUEST=-1003;
const int Errors::ERROR_RPC_INVALID_PARAMS=-1004;
const int Errors::ERROR_RPC_INTERNAL_ERROR=-1005;

Errors::_init::_init(){
    error_msgs[ERROR_RPC_JSON_PARSE_ERROR]="Fail to parse json";
}

std::string Errors::ErrorMsg(int error_code) {
  if (error_msgs.find(error_code) == error_msgs.end()) {
    return "";
  }
  return error_msgs[error_code];
}
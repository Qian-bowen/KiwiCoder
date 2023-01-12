#include "kiwi/include/exception.h"

KiwiException::KiwiException(int code):code(code){}


KiwiException::KiwiException(int code,const std::string& msg):code(code),msg(msg){}

KiwiException::KiwiException(const std::string& msg):code(0),msg(msg){}

KiwiException::~KiwiException()throw(){}

const char *KiwiException::what() const throw(){
    return this->msg.c_str();
}

int KiwiException::GetCode()const{
    return this->code;
}

const std::string& KiwiException::GetMsg()const{
    return this->msg;
}
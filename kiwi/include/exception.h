#ifndef Kiwi_EXCEPTION_H
#define Kiwi_EXCEPTION_H

#include<exception>

#include "error.h"

class KiwiException:public std::exception{
public:
    KiwiException(int code);
    KiwiException(int code,const std::string& msg);
    KiwiException(const std::string& msg);
    virtual ~KiwiException() throw();

    virtual const char *what() const throw();

    int GetCode()const;
    const std::string& GetMsg()const;

private:
    int code;
    std::string msg;
};

#endif
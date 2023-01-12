#ifndef KRPC_INVOKE_HANDLER_H
#define KRPC_INVOKE_HANDLER_H

#include "kiwi/include/procedure.h"

class InvokeHandler{
public:
    InvokeHandler()=default;
    ~InvokeHandler()=default;
    virtual void HandleMethodCall(Procedure &proc, const json &input, json &output)=0;
    virtual void HandleNotificationCall(Procedure &proc, const json &input)=0;
};

#endif
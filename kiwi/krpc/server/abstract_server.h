#ifndef KRPC_ABSTRACTSERVER_H
#define KRPC_ABSTRACTSERVER_H

#include "kiwi/include/procedure.h"
#include "base_server.h"
#include "invoke_handler.h"
#include "rpc_protocol.h"
#include "protocol_factory.h"
#include<map>

template<class T>
class AbstructServer:InvokeHandler{
    typedef void (T::*methodPtr_t)(const json &params,json &result);
    typedef void (T::*notificationPtr_t)(const json &params);
public:
    explicit AbstructServer(BaseServer &connector, procedure_t protocol_type):connection(connector){
        this->handler=ProtocolFactory::CreateProtocolHandler(protocol_type,*this);
        connection.SetHandler(this->handler);
    }
    virtual ~AbstructServer()=default;

    bool StartListening() { return connection.StartListening(); }
    bool StopListening() { return connection.StopListening(); }

    virtual void HandleMethodCall(Procedure &proc, const json &input, json &output)override{
        T *instance = dynamic_cast<T *>(this);
        (instance->*methods[proc.GetProcedureName()])(input,output);
    }

    virtual void HandleNotificationCall(Procedure &proc, const json &input)override{
         T *instance = dynamic_cast<T *>(this);
        (instance->*notifications[proc.GetProcedureName()])(input);
    }

protected:
    bool AddMethod(const Procedure &proc,mentodPtr_t ptr){
        handler->AddProcedure(proc);
        methods[proc.GetProcedureName()] = ptr;
    }

    bool AddNotification(const Procedure &proc,notificationPtr_t ptr){
        handler->AddProcedure(proc);
        notifications[proc.GetProcedureName()] = ptr;
    }

private:
    BaseServer &connection;
    std::shared_ptr<BaseProtocolHandler> handler;
    std::map<std::string,methodPtr_t> methods;
    std::map<std::string,notificationPtr_t> notifications;
};

#endif
#ifndef KRPC_PROTOCOL_FACTORY_H
#define KRPC_PROTOCOL_FACTORY_H

#include "protocol.h"
#include "rpc_protocol.h"

class ProtocolFactory{
public:
    static BaseProtocolHandler* CreateProtocolHandler(procedure_t type, InvokeHandler &handler){
        BaseProtocolHandler* protocol_handler=nullptr;
        switch(type){
        case RPC_JSON_COMM:
            protocol_handler=new RPCProtocolHandler(handler);
        }
        return protocol_handler;
    }
};


#endif
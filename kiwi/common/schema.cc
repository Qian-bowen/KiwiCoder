#include "kiwi/include/schema.h"

json ParseProtoRPC(std::string proto_str){
    json data = json::parse(proto_str);
    return data;
}

bool ValidateProtoRPC(json proto_json){

}
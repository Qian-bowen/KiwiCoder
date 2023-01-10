#ifndef Kiwi_SCHEMA_H
#define Kiwi_SCHEMA_H

#include<nlohmann/json.hpp>

using json = nlohmann::json;

// RPC Schema Example
// using json format
// {
//   "service": "$service name$",
//   "methods": [
//     {
//       "name": "$method1$",
//       "params": {"$param1$": $value1$, "$param2$": $value2$},
//       "return": $value$
//     },
//     {
//       "name": "$method2$",
//       "params": {"$param1$": $value1$},
//       "return": $value$
//     }
//   ]
// }

// Convert RPC Json string to Json object
json ParseProtoRPC(std::string proto_str);

// Validate Json object based on schema
bool ValidateProtoRPC(json proto_json);

#endif
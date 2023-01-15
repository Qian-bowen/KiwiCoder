#ifndef Kiwi_PROCEDURE_H
#define Kiwi_PROCEDURE_H

#include<nlohmann/json.hpp>
#include<string>
#include "kiwi/include/types.h"

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

class Procedure{
public:
    const std::string& GetProcedureName()const;
    procedure_t GetProcedureType()const;

};

#endif
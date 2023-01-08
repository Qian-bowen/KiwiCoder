#include<string>
#include "object.h"

#ifndef Kiwi_STRINGOBJECT_H
#define Kiwi_STRINGOBJECT_H

class KiwiStringObject:public KiwiVarObject{
    std::string ob_sval;
    int ob_sstate;
};


#endif
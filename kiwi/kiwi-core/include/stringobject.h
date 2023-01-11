#ifndef Kiwi_STRINGOBJECT_H
#define Kiwi_STRINGOBJECT_H

#include<string>
#include "kiwi/kiwi-core/include/object.h"

class KiwiStringObject:public KiwiVarObject{
    std::string ob_sval;
    int ob_sstate;
};


#endif
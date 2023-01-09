#ifndef Kiwi_LISTOBJECT_H
#define Kiwi_LISTOBJECT_H

#include<vector>
#include "kiwi-core/include/object.h"

class KiwiListObject:public KiwiVarObject{
    std::vector<KiwiObject*> ob_item; 
};

#endif
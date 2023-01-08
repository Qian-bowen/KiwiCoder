#include<vector>
#include "object.h"

#ifndef Kiwi_LISTOBJECT_H
#define Kiwi_LISTOBJECT_H

class KiwiListObject:public KiwiVarObject{
    std::vector<KiwiObject*> ob_item; 
};

#endif
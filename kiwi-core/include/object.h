#include<string>

#ifndef Kiwi_OBJECT_H
#define Kiwi_OBJECT_H

class KiwiTypeObject{
    std::string tp_name;
    int tp_itemsize;
};

class KiwiObject{
    int ob_refcnt;
    KiwiTypeObject *ob_type;
};

class KiwiVarObject:public KiwiObject{
    int ob_size;
};


#endif
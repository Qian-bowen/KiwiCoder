#ifndef KRPC_SERVERSTUBGEN_H
#define KRPC_SERVERSTUBGEN_H

#include "kiwi/krpc/stub_gen.h"

class ServerStubGen:public StubGen{
public:
    explicit ServerStubGen():StubGen(){}

    virtual void GenStub() override;

};

#endif
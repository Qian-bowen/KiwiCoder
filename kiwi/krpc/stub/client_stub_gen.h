#ifndef KRPC_CLIENTSTUBGEN_H
#define KRPC_CLIENTSTUBGEN_H

#include "kiwi/krpc/stub_gen.h"

class ClientStubGen:public StubGen{
public:
    explicit ClientStubGen():StubGen(){}

    virtual void GenStub() override;

private:
    inline std::string GenMacroName();


};

#endif
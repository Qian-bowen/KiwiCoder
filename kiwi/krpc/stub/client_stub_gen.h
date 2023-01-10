#ifndef KRPC_CLIENTSTUBGEN_H
#define KRPC_CLIENTSTUBGEN_H

#include "kiwi/krpc/stub/stub_gen.h"

class ClientStubGen:public StubGen{
public:
    explicit ClientStubGen():StubGen(){}

    std::string GenStub() override;
    std::string GenStubClassName() override;
private:
    inline std::string GenMacroName();


};

#endif
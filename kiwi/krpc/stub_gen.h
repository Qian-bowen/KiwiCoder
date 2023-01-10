#ifndef KRPC_STUBGEN_H
#define KRPC_STUBGEN_H

#include <string>
#include <vector>
#include "kiwi/include/file.h"

struct ServiceInfo{
    std::string name;
};

class StubGen: public FileGenerator{
public:
    explicit StubGen(){}
    virtual ~StubGen() = default;

    virtual void GenStub() = 0;

protected:
    ServiceInfo service_info;

};

#endif
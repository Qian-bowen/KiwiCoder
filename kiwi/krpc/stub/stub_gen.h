#ifndef KRPC_STUBGEN_H
#define KRPC_STUBGEN_H

#include <string>
#include <vector>

struct ServiceInfo{
    std::string name;
};

class StubGen{
public:
    explicit StubGen(){}
    virtual ~StubGen() = default;

    virtual std::string GenStub() = 0;
    virtual std::string GenStubClassName() = 0;
protected:
    ServiceInfo service_info;

};

#endif
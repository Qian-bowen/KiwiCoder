#include "kiwi/include/util.h"
#include "kiwi/krpc/stub/client_stub_gen.h"

void ClientStubGen::GenStub(){

}

std::string ClientStubGen::GenMacroName(){
    std::string service_name=service_info.name;
    for(auto& ch:service_name){
        ch = static_cast<char>(toupper(ch));
    }
    service_name.append("_H");
    return service_name;
}

std::string ClientStubTemplate(const std::string& macro_name, const std::string& stub_class_name){
    std::string template_str = R"()";
    ReplaceAll(template_str,"",macro_name);
    ReplaceAll(template_str,"",stub_class_name);
    return template_str;
}


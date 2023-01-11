#ifndef Kiwi_UTIL_H
#define Kiwi_UTIL_H

#include<string>

// Replace all occurance of substrng 'from' in string 'template_str' to substring 'to'
inline void ReplaceAll(std::string& template_str, const std::string& from, const std::string& to){
    size_t pos = template_str.find(from);
    while (pos != std::string::npos) {
        template_str.replace(pos, from.length(), to);
        pos = template_str.find(from, pos + template_str.length());
    }
}

#endif
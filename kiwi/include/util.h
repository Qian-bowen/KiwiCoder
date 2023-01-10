#ifndef Kiwi_UTIL_H
#define Kiwi_UTIL_H

#include<string>
#include<regex>

// Replace all occurance of substrng 'from' in string 'template_str' to substring 'to'
inline void ReplaceAll(std::string& template_str, const std::string& from, const std::string& to){
    template_str = std::regex_replace(template_str,std::regex(from),to);
}

#endif
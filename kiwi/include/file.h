#ifndef Kiwi_FILE_H
#define Kiwi_FILE_H

#include<string>

class FileGenerator{
public:
    explicit FileGenerator(const std::string& filename);
    virtual ~FileGenerator();

};

#endif
#ifndef Kiwi_FILE_H
#define Kiwi_FILE_H

#include<string>

class FileGenerator{
public:
    explicit FileGenerator(const std::string& filename);
    virtual ~FileGenerator();

};

class StreamWriter{
public:
    bool Write(const std::string &source, int fd);
};

class StreamReader{
public:
    StreamReader(unsigned int buffer_size);
    virtual ~StreamReader();
    bool Read(std::string &target, int fd, char delimiter);
private:
    unsigned int buffer_size;
    char *buffer;
};

#endif
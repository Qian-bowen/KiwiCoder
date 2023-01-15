#include "kiwi/include/file.h"
#include <unistd.h>

bool StreamWriter::Write(const std::string &source, int fd){
    int write_byte;
    long long total_size=source.size();
    long long remain_size=source.size();
    do{
        write_byte=write(fd,source.c_str()+total_size-remain_size,remain_size);
        if(write_byte<0){
            return false;
        }else{
            remain_size-=write_byte;
        }
    }while(remain_size>0);
    return true;
}

StreamReader::StreamReader(unsigned int buffer_size):buffer_size(buffer_size){
    this->buffer=new char[buffer_size];
}

StreamReader::~StreamReader(){
    delete [] buffer;
}

bool StreamReader::Read(std::string &target, int fd, char delimiter){
    int read_byte;
    // read file till the delimiter
    do{
        read_byte=read(fd,this->buffer,buffer_size);
        if(read_byte<0){
            return false;
        }else{
            target.append(buffer,read_byte);
        }
    }while(memchr(buffer, delimiter, read_byte) == nullptr);\
    target.pop_back();
    return true;
}
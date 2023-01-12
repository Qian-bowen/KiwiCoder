#include "base_server.h"
#include "kiwi/include/constants.h"
#include "kiwi/include/file.h"
#include <unistd.h>
#include <fcntl.h>

// BaseServer

BaseServer::BaseServer(int thread_num):thread_pool(thread_num),thread_num(thread_num),is_running(false){

}

BaseServer::~BaseServer(){
    this->StartListening();
}

bool BaseServer::StartListening(){
    if(this->is_running){
        return false;
    }
    if(!this->InitializeListener()){
        return false;
    }
    this->is_running=true;
    this->listener_thread=std::unique_ptr<std::thread>(new std::thread(&BaseServer::ListenLoop,this));
    return true;
}

bool BaseServer::StopListening(){
    if (!this->is_running){
        return false;
    }

    this->is_running = false;
    this->listener_thread->join();
    return true;
}

void BaseServer::ListenLoop(){
    while(this->is_running){
        int fd=this->GetFrontConnection();
        if(fd<0){
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            continue;
        }
        if(this->thread_num>0){
            this->thread_pool.enqueue(&BaseServer::HandleConnection,this,fd);
        }else{
            this->HandleConnection(fd);
        }
    }
}

void BaseServer::HandleRequest(const std::string &request,std::string &response){
    this->handler->HandleRequest(request,response);
}

void BaseServer::SetHandler(std::shared_ptr<BaseProtocolHandler> handler){
    this->handler=handler;
}
#ifndef KRPC_BASESERVER_H
#define KRPC_BASESERVER_H

#include "protocol.h"
#include "kiwi/include/thread_pool.h"

#include<string>
#include<memory>

class BaseServer{
public:
    explicit BaseServer(int thread_num);
    virtual ~BaseServer();

    virtual bool StartListening()=0;
    virtual bool StopListening()=0;

    virtual bool InitializeListener() = 0;
    virtual int GetFrontConnection()=0;
    virtual void HandleConnection(int connection)=0;

    void HandleRequest(const std::string &request,std::string &response);
    void SetHandler(std::shared_ptr<BaseProtocolHandler> handler);

private:
    void ListenLoop();

private:
    std::shared_ptr<BaseProtocolHandler> handler;
    std::unique_ptr<std::thread> listener_thread;
    ThreadPool thread_pool;
    int thread_num;
    bool is_running;
};

#endif
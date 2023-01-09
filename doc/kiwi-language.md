# Kiwi Language Design

Kiwi语言会支持生物实验标准API（Standard Bio Experiment API，BES），用户可以通过Kiwi来编写实验流程。需要编写在一个文件中，文件名以.kw结尾。部分SBE有默认的内置实现，部分没有。

用户标注需要自己实现的SBE，KiwiCoder会用rpcgen（python）生成用Python或C语言编写的RPC脚手架代码，用户导出该框架，实现对应函数即可。

RPC 框架代码包含两部分，RPC和Mock RPC，对应实际运行和模拟运行功能。用户可以根据需求实现。

KiwiCoder会将kw文件编译成字节码运行。

KiwiCoder可以导出一份report文件，文件中是自然语言描述的实验流程。

Kiwi最大的优势是将实验的代码描述、自然语言描述相结合，将代码逻辑与边缘设备的逻辑实现进行解耦。



bes列表


# Kiwi Language Design

Kiwi：生物实验语言，用代码描述实验流程。Kiwi是动态语言，编译成字节码，运行在虚拟机中。

Kiwi-native：描述实验流程的自然语言，可以由Kiwi语言生成。

SBE：生物实验标准API（SBE），是一套定义的标准接口。

Kiwi-IDL：用Json格式记录的SBE函数，rpcgen工具可以根据IDL生成RPC框架。

krpc：RPC框架生成工具，用于实验设备与控制代码交互。

Kdb：Kiwi语言的调试工具。

KiwiWatch：实验监控系统，有UI界面。

KiwiCoder：包含上述程序的开发工具。

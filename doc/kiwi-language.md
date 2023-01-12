# Kiwi Language Design

Kiwi：生物实验语言，用代码描述实验流程。Kiwi是动态语言，编译成字节码，运行在虚拟机中。

Kiwi-native：描述实验流程的自然语言，可以由Kiwi语言生成。

SBE：生物实验标准API（SBE），是一套定义的标准接口。

Kiwi-IDL：用Json格式记录的SBE函数，krpc工具可以根据Json生成RPC框架。

krpc：RPC框架生成工具，用于实验设备与控制代码交互。

Kdb：Kiwi语言的调试工具。

KiwiWatch：实验监控系统，有UI界面。

KiwiCoder：包含上述程序的开发工具。

同名SBE函数生成的Kiwi-IDL中，它们对应的rpc方法是不同的，因为SBE名字相同，但可以由不用硬件实现。




函数支持多个返回值。



变量标识符号
<watch,<.>>:监控变量值。点符号表示监视后面的变量。
<alarm,<.,lg,5>>: 告警。第二个位置的lg表示大于，第三个位置的5表示阈值。

函数标识符号（仅SBE函数）
<SBE>：SBE函数标配符号，必须在函数最前面
<watch,<p1,r2>>: 监控变量值。p1表示函数的第一个参数，r2表示第2个返回值。
<alarm,<p1,lg,5>,<r2,eq,"test">>: 告警。

标识符号必须紧跟在变量声明或定义的最前面
<watch,<.>> int value
<SBE><watch,<p1,r2>><alarm,<p1,lg,5>,<r2,eq,"test">> func(int p1, int p2)->(int r1, string r2)

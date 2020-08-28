# multiprocessingpy
Python 多进程处理框架
采用多进程方式并行化处理任务的框架，多进程间利用消息队列进行通信，该框架只可以单机使用

Operator：每个操作都看做是一个算子,一共包括3中算子Datasource，Processor和Dump
Datasource： 和数据源相关，一般是输入型算子
Processor: 处理型算子一般处于中间操作
Dump ： 输出型算子，一般对操作结果持久化

使用流程
1. 自定义个自己个 Datasource，Processor，Dump算子
2. 自定义Workflow对象，该对象是整个工作流的宏观组织对象
3. 执行Workflow 的start方法

例子： 参看test/test_workflow.py

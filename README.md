# Debate-of-Thoughts(DoT)

Search and RAG are just tools, verification is the key. The more the truth is debated, the clearer it becomes.


目前分为以下几个大的模块:

Debater：即Agent智能体，可以集成市面上的多智能体或者RAG工具等，主要作用是生成node（round）中的内容
![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240318215900.png)


Node：即round轮次，分为初始的轮次和后续的轮次，后续的轮次需要传入连接轮次。
![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240318215830.png)

Observer：负责记录和更新全局信息，包括全局的消息信息，节点的关系（矩阵），节点的分数（字典），节点的影响力（字典）


Judge：负责下一个轮次选择什么辩手，下个轮次针对哪个Node，是选择支持还是反对。
# Debate-of-Thoughts(DoT)

**Search and RAG are just tools, verification is the key. The more the truth is debated, the clearer it becomes.**

## Roadmaps
基础性的框架搭建与最小闭环已经实现了，接下来中需要对每个模块进行一定的优化，重要性排行如下：

### Judege
评分模块和策略模块需要用Agent或者机器学习方法实现

### Debater
- 集成Langchain Agent
- 集成MetaGPT的单Agent
- 集成RAG Debater
- 集成Search Debater


### Node
- 思考一下汇总Node
- 优化提示词

### Graph
思考一下能在Neo4j中实现怎么样的再利用

## 模块介绍
目前分为以下几个大的模块:

- Debater：即Agent智能体，可以集成市面上的多智能体或者RAG工具等，作用是生成Node中的内容。
- Node：即问答轮次，分为初始的轮次和后续的轮次，后续的轮次需要传入连接轮次并用边属性表示支持与反对。
- Observer：负责记录和更新全局信息，包括全局的消息信息，节点的关系（矩阵），节点的分数（字典），节点的影响力（字典）。
- Judge：负责下一个轮次选择什么辩手，下个轮次针对哪个Node，是选择支持还是反对,并且给每一轮生成的答案进行评分。
- Graph：负责上传Observer中的node数据到图数据库neo4j中，并实现后续的分析
![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240323101420.png)

![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240318215900.png)




![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240318215830.png)








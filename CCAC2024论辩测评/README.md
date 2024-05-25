# 自主论辩智能体
欢迎来到CCAC2024论辩测评，以下是该任务的测评流程

# 环境与依赖
首先，参赛选手需要依次执行以下命令，配置虚拟环境并安装环境依赖
```
conda create -n CCAC python==3.10
```

```
pip install -r requirements.txt
```

# API配置
然后，参赛选手需要执行以下命令，并在生成的.env填写自己的API-KEY，完成基本配置
```
 cp .env_template  .env
```

# 自主论辩智能体设计
[基准智能体](ccacbasedebater.py)是代表正方的基准智能体，无需进行任何改动。

[参赛智能体](ccacdebater.py)代表反方，需要参赛选手自行设计，可以从大模型，提示词，智能体工具或者智能体框架等多方面进行改进。


# 执行测评脚本
在完成参赛智能体的设计之后,直接运行[测评脚本](CCAC论辩测评脚本.ipynb)即可在logs文件夹下，生成两个包含内容信息日志文件。(如下两个日志文件可作为参考案例)

![image.png](https://kashiwa-pic.oss-cn-beijing.aliyuncs.com/20240525103915.png)
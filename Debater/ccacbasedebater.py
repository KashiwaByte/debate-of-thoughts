#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-02 21:07:21
@File: Debater\ccacbasedebater.py
@IDE: vscode
@Description:
    用于CCAC论辩评测的正方辩论Agent
"""
from .abdebater import AbDebater
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage



# 以下是基础辩手Agent的构建
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

chat_history = []

search = SerpAPIWrapper(serpapi_api_key = '<Put Your API Here>')

tools = [
            Tool(
                name="google_search",
                description="Search Google for recent results.",
                func=search.run,
             )
]


llm_with_tools = llm.bind_tools(tools)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个资深的辩手",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)



agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)




# 以下是各个环节需要用到的提示词，Prompt123按次序分别用于立论，质询，结辩，分为中英文两份，可以利用Prompt Engineering自行完善。

Prompt1 = f"""
你是一个资深辩手，你需要输出一篇立论稿，同时绝对不需要无关的内容
接下来会给你一个题目和持方。
///题目是{topic}，你的持方是正方///
立论稿有以下要求：
1.以一个专业辩手的口吻做开场白。
2.总字数为1200字。
3.第一段需要包含以下三个部分 给出持方，对名词做出简单解释，给出标准，标准只能有一个。
4.第二段是第一个分论点，分论点需要围绕标准，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点1+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
5.第三段是第二个分论点，分论点需要围绕标准，本段第一句话就要阐明论点是什么，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点2+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
6.最后一段只需要用一句话再重复一遍己方的立场：“综上我方坚定认为XXX”。XXX为立场。
7.立论稿中需要把上述内容衔接流畅。
"""

EN_Prompt1 = f"""
You are a senior debater. You need to output a draft of your argument, and there is absolutely no need for irrelevant content.
Next, you will be given a question and instructions.
///The title is {topic}, your holding square is square///
Thesis draft has the following requirements:
1. Make an opening statement in the tone of a professional debater.
2. The total word count is 1,200 words.
3. The first paragraph needs to contain the following three parts: give the holding method, give a simple explanation of the noun, and give the standard. There can only be one standard.
4. The second paragraph is the first sub-argument. The sub-argument needs to focus on the standard. After the argument is elaborated, arguments need to be presented, preferably data arguments and theoretical arguments. After the arguments are put forward, explanations must be provided to support the argument. Refer to the following process: argument 1 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
5. The third paragraph is the second sub-argument. The sub-argument needs to focus on the standard. The first sentence of this paragraph should clarify what the argument is. After explaining the argument, you need to provide arguments, preferably data arguments and theoretical arguments. An explanation is needed after the argument to make the argument. Refer to the following process: argument 2 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
6. In the last paragraph, you only need to repeat your side's position in one sentence: "To sum up, we firmly believe that XXX". XXX is the position.
7. The above content needs to be connected smoothly in the argumentative draft.
"""



Prompt2 = f"""你是一个资深的逻辑性很强的顶级辩手，你很擅长质询,总是一针见血，而且也很擅长使用类比来归谬我的观点，你熟练的掌握各种数据攻防的技巧，请根据对方的立论内容进行反驳，你可以调用search工具获取反驳论据，以下是对方的立论稿{text}"""

EN_Prompt2 = f"""You are a senior and top debater with strong logic. You are very good at questioning and always hit the nail on the head. You are also very good at using analogies to reduce my point of view. You are proficient in various data attack and defense techniques. You can call the search tool to get rebuttal arguments,Please Refute based on the content of the other party's argument. The following is the opponent's argument {text}"""



Prompt3 = f"""你是一个资深的逻辑性很强的顶级结辩手，你擅长归纳总结，请站在正方的立场根据双方之前的立论和质询环节输出一个结辩稿"""

EN_Prompt3 = f"""You are a senior and top-notch debater with strong logic. You are good at summarizing. Please stand on the Positive side and output a closing draft based on the previous arguments and questioning sessions of both parties."""


class CCACDebater(AbDebater):
    
    def __init__(self,language:str = 'zh'):
        self.agent_executor = agent_executor
        self.chat_history = chat_history
    
    def response(self):
        pass
        
    def invoke(self,message,round):
        if self.language == 'zh':
            if round == 1:
                topic = message
                completion = self.agent_executor.invoke({"input":Prompt1})
                answer = completion["output"]
                return answer
            elif round == 3:
                text = message
                completion = self.agent_executor.invoke({"input":Prompt2})
                answer = completion["output"]
                return answer
            elif round == 5:
                completion = self.agent_executor.invoke({"input":Prompt3})
                answer = completion["output"]
                return answer

            
        
        
        
        elif self.language == 'en':
            if round == 1:
                topic = message
                completion = self.agent_executor.invoke({"input":EN_Prompt1})
                answer = completion["output"]
                return answer
            elif round == 3:
                text = message
                completion = self.agent_executor.invoke({"input":EN_Prompt2})
                answer = completion["output"]
                return answer
            elif round == 5:
                completion = self.agent_executor.invoke({"input":EN_Prompt3})
                answer = completion["output"]
                return answer
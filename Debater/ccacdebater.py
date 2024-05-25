#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-07 19:35:26
@File: Debater\ccacdebater.py
@IDE: vscode
@Description:
     用于CCAC论辩评测的反方可定制辩论Agent范例
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

search = SerpAPIWrapper(serpapi_api_key = 'fe7e2de72185aa0cc1595f5eb784daac2a3497fe405c668efa612e78cbfaff13')

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
# topic在立论环节为双方立论的辩题，context在驳论环节为对方的立论稿，在结辩环节为全场比赛的内容
class CCACDebater(AbDebater):
    
    def __init__(self,language:str = 'zh'):
        self.agent_executor = agent_executor
        self.language = language
    
    def response(self):
        pass
        
    def invoke(self,message,round):
        if self.language == 'zh':
            if round == 2:
                topic = message
                Prompt1 = f"""
                            你是一个资深辩手，你需要输出一篇立论稿，同时绝对不需要无关的内容
                            接下来会给你一个题目和持方。
                            ///题目是{topic}，你的持方是反方///
                            立论稿有以下要求：
                            1.第一段需要包含以下三个部分 给出持方，对名词做出简单解释，给出标准，标准只能有一个。
                            2.第二段是第一个分论点，分论点需要围绕标准，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点1+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
                            3.第三段是第二个分论点，分论点需要围绕标准，本段第一句话就要阐明论点是什么，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点2+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
                            4.立论稿中需要把上述内容衔接流畅。
                            """
                completion = self.agent_executor.invoke({"input":Prompt1})
            elif round == 4:
                context = message
                Prompt2 = f"""你是一个资深的逻辑性很强的顶级辩手，你很擅长驳论,请根据对方的立论内容进行反驳，以下是对方的立论稿{context}"""
                completion = self.agent_executor.invoke({"input":Prompt2})
            elif round == 6:
                context = message
                Prompt3 = f"""请站在反方的立场，总结双方之前的环节信息输出一个结辩稿，结辩不需要使用搜索工具，以下是之前的环节信息{context}"""
                completion = self.agent_executor.invoke({"input":Prompt3})
            answer = completion["output"]
            return answer
            
        
        
        
        elif self.language == 'en':
            if round == 2:
                topic = message
                EN_Prompt1 = f"""
                                You are a senior debater. You need to output a draft of your argument, and there is absolutely no need for irrelevant content.
                                Next, you will be given a question and instructions.
                                ///The topic is {topic}, and your position is negative///
                                Thesis draft has the following requirements:
                                1. The first paragraph needs to contain the following three parts: give the holding method, give a simple explanation of the noun, and give the standard. There can only be one standard.
                                2. The second paragraph is the first sub-argument. The sub-argument needs to focus on the standard. After the argument is elaborated, arguments need to be presented, preferably data arguments and theoretical arguments. After the arguments are put forward, explanations must be provided to support the argument. Refer to the following process: argument 1 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
                                3. The third paragraph is the second sub-argument. The sub-argument needs to focus on the standard. The first sentence of this paragraph should clarify what the argument is. After explaining the argument, you need to provide arguments, preferably data arguments and theoretical arguments. An explanation is needed after the argument to make the argument. Refer to the following process: argument 2 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
                                4. The above content needs to be connected smoothly in the argumentative draft.
                             """
                completion = self.agent_executor.invoke({"input":EN_Prompt1})
            elif round == 4:
                context = message
                EN_Prompt2 = f"""You are a senior and top debater with strong logic. You are very good at refutation. Please refute based on the content of the other party's argument. The following is the opponent's argument {context}"""
                completion = self.agent_executor.invoke({"input":EN_Prompt2})
            elif round == 6:
                context = message
                EN_Prompt3 = f"""Please stand on the opposing side, summarize the previous link information of both parties and output a closing draft. There is no need to use search tools for the closing argument. The following is the previous link information {context}"""
                completion = self.agent_executor.invoke({"input":EN_Prompt3})
            answer = completion["output"]
            return answer
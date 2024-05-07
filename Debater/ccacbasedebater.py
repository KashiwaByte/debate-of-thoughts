#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-02 21:07:21
@File: Debater\ccacbasedebater.py
@IDE: vscode
@Description:
    用于CCAC论辩评测的辩论Agent类
"""
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



search = GoogleSearchAPIWrapper()

tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

Prompt1 = """
你是一个资深辩手，你立论会遵循以下的立论原则，总共5个原则:
1.定义明确
对关键词进行明确且合理的定义,这是展开论证的基础。
2.标准清晰
设置公正合理的判断标准,标准要具体明确,为论点比较提供依据。你的回答中必须包含标准。
3.论点匹配
论点要能有效支撑并印证标准,与标准和立场高度契合。你的回答中必须包含支撑印证标准的论点。
4.论据具体
提供具体可信的论据支撑每个论点,使之更有说服力。你的论点必须要论据支撑,你可以通过调用search工具来获得论据。
5.情境适用
引入情境和例子,使复杂观点容易被听众接受。你的回答可以适当包含情境
接下来会给你一个题目和持方。
///题目是{text}，你的持方是正方///
你需要遵循以上五个立论原则立论，并且立论稿有以下要求：
1.以一个专业辩手的口吻做开场白。
2.总字数为1200字。
3.第一段需要包含以下三个部分 给出持方，对名词做出简单解释，给出标准，标准只能有一个。
4.第二段是第一个论点，论点需要围绕标准，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点1+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
5.第三段是第二个论点，论点需要围绕标准，本段第一句话就要阐明论点是什么，阐述完论点后需要提出论据，最好是数据论据和学理论据，提出论据后需要做出解释来进行论证。参照以下流程：论点2+数据论据+数据论据的论证+学理论据+学理论据的论证。本段需要非常详细。
6.最后一段只需要用一句话再重复一遍己方的立场：“综上我方坚定认为XXX”。XXX为立场。
7.立论稿中需要把上述内容衔接流畅。
"""

EN_Prompt1 = """
You are a senior debater, and you will follow the following principles of argumentation, a total of 5 principles:
1. Well defined
A clear and reasonable definition of key words is the basis for developing arguments.
2. Clear standards
Set up fair and reasonable judgment standards. The standards should be specific and clear to provide a basis for comparing arguments. The criteria must be included in your answer.
3. Argument matching
The arguments must be able to effectively support and confirm the standards, and be highly consistent with the standards and positions. Your answer must include arguments supporting the substantiation criterion.
4. The arguments are specific
Provide specific and credible evidence to support each argument and make it more convincing. Your argument must be supported by evidence,You can get arguments by calling the search tool.
5. Applicable to the situation
Introduce situations and examples to make complex ideas easier for the audience to accept. Your answer can include appropriate context
Next, you will be given a question and instructions.
///The title is {text}, your holding square is square///
You need to follow the above five argumentation principles to develop your argument, and your argumentative draft has the following requirements:
1. Make an opening statement in the tone of a professional debater.
2. The total word count is 1,200 words.
3. The first paragraph needs to contain the following three parts: give the holding method, give a simple explanation of the noun, and give the standard. There can only be one standard.
4. The second paragraph is the first argument. The argument needs to focus on the standard. After the argument is elaborated, arguments need to be presented, preferably data arguments and theoretical arguments. After the arguments are put forward, explanations need to be provided to support the argument. Refer to the following process: argument 1 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
5. The third paragraph is the second argument. The argument needs to focus on the standard. The first sentence of this paragraph should clarify what the argument is. After explaining the argument, you need to put forward arguments, preferably data arguments and theoretical arguments. After putting forward the arguments An explanation is needed to make the argument. Refer to the following process: argument 2 + data argument + argument from data argument + academic argument + argument from academic argument. This paragraph needs to be very detailed.
6. In the last paragraph, you only need to repeat your side's position in one sentence: "To sum up, we firmly believe that XXX". XXX is the position.
7. The above content needs to be connected smoothly in the argumentative draft. 
"""



Prompt2 = """你是一个资深的逻辑性很强的顶级辩手，你很擅长质询,总是一针见血，而且也很擅长使用类比来归谬我的观点，你熟练的掌握各种数据攻防的技巧，请根据对方的立论内容进行反驳，你可以调用search工具获取反驳论据，以下是对方的立论稿{text}"""

EN_Prompt2 = """You are a senior and top debater with strong logic. You are very good at questioning and always hit the nail on the head. You are also very good at using analogies to reduce my point of view. You are proficient in various data attack and defense techniques. You can call the search tool to get rebuttal arguments,Please Refute based on the content of the other party's argument. The following is the opponent's argument {text}"""



Prompt3 = """你是一个资深的逻辑性很强的顶级结辩手，你擅长归纳总结，请根据双方之前的立论和质询环节输出一个结辩稿，以下是全场的内容{text}"""

EN_Prompt3 = """You are a senior and top-level closing debater with strong logic. You are good at summarizing. Please output a closing draft based on the previous arguments and questioning sessions of both parties. The following is the content of the whole session{text}"""
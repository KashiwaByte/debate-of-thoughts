#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-25 19:44:20
@File: Debater\Dlangchain\searchchain.py
@IDE: vscode
@Description:
    Langchain SearchChain
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '..')
sys.path.append(relative_path)
from Debater import AbDebater

from langchain_community.utilities import SearchApiAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_community.utilities import SearchApiAPIWrapper
from langchain_openai import OpenAI

class SearchChain(AbDebater):
    
    def __init__(self,search_api,openai_api):
        os.environ["SEARCHAPI_API_KEY"] = search_api
        os.environ["OPENAI_API_KEY"] = openai_api
        llm = OpenAI(temperature=0)
        search = SearchApiAPIWrapper()
        tools = [
            Tool(
                name="Intermediate Answer",
                func=search.run,
                description="useful for when you need to ask with search",
            )
        ]
        self.searchchain = initialize_agent(
            tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
    
    def response(self,messages):
        pass
        
    def invoke(self,messages):
        message = messages[1]["content"]
        print(message)
        answer = self.searchchain.run(message)
        return answer
    
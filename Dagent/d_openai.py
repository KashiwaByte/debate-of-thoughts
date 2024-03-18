#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 08:51:15
@File: Dagent\openaillm.py
@IDE: vscode
@Description:
    openai大语言模型
"""
from .abllm import AbLLM

from openai import OpenAI



class D_Openai(AbLLM):
    
    def __init__(self, model: str,api_key):
        super().__init__(model)
        self.client = OpenAI(api_key=api_key)
        
        
    def response(self, messages):
        
        completion = self.client.chat.completions.create(
        model=self.model,
        messages=messages,
      )
        return completion
        
    def invoke(self,messages):
        completion = self.response(messages)
        answer = completion.choices[0].message.content
        return answer
    
    

    
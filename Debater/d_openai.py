#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 21:57:01
@File: Debater\d_openai.py
@IDE: vscode
@Description:
     openai大语言模型
"""
from .abdebater import AbDebater

from openai import OpenAI



class D_Openai(AbDebater):
    
    def __init__(self, api_key,model: str= "gpt-3.5-turbo"):
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
    
    

    
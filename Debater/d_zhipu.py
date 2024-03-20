#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-20 23:26:21
@File: Debater\d_zhipu.py
@IDE: vscode
@Description:
    智谱大语言模型
"""
from .abdebater import AbDebater

from zhipuai import ZhipuAI

class D_Zhipuai(AbDebater):
    
    def __init__(self, api_key,model: str= "glm-4"):
        super().__init__(model)
        self.client =ZhipuAI(api_key=api_key)
        
        
    def response(self, messages): 
        completion = self.client.chat.completions.create(
        model=self.model,
        messages=messages,
      )
        return completion
        
    def invoke(self,messages):
        completion = self.response(messages)
        answer = completion.choices[0].message
        return answer
    
    




#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 10:07:14
@File: Dnode\initialnode.py
@IDE: vscode
@Description:
    最初节点类
"""

from .abnode import AbNode
class InitNode(AbNode):
    
    def __init__(self,topic,debater,language:str ='zh'):
        self.round_id = 1
        self.language = language
        self.topic = topic
        self.depth = 0
        self.debater=debater
        self.get_content()
       
        
        
    def get_content(self):
        if self.language == "zh":
            init_messages=[
                    {"role": "system", "content": "你是一个有用的助手，请根据以下问题输出一个观点明确的回答，绝对不得表达模糊不清的观点"},
                    {"role": "user", "content": ""},
                        ]
        elif self.language == "en":
            init_messages=[
                    {"role": "system", "content": "You are a useful assistant. Please provide a clear answer to the following questions. Never express vague opinions."},
                    {"role": "user", "content": ""},
                        ]
        init_messages[1]['content'] = self.topic
        self.context = init_messages
        answer = self.debater.invoke(init_messages)
        self.content = answer
       

    
    
  
#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-05 18:32:06
@File: Dnode\ccacnode.py
@IDE: vscode
@Description:
    用于ccac测评的基础节点类
"""
from .abnode import AbNode
from Debater import D_Openai

class CCACNode(AbNode):
    
    
    def __init__(self,round:int,debater,language:str = "zh"):
        self.round = round
        self.debater=debater
        self.language = language
        self.get_topic()
        self.get_content()
        pass
    
    def get_round_name(self):
        """用于获取该环节名称"""
        if self.round == 1:
            self.round_name = "正方立论"
        elif self.round == 2:
            self.round_name = "反方立论"
        elif self.round == 3:
            self.round_name = "正方驳论"
        elif self.round == 4:
            self.round_name = "反方驳论"
        elif self.round == 5:
            self.round_name = "正方结辩"
        elif self.round == 6:
            self.round_name = "反方结辩"

    
    def get_topic(self):
        return super().get_topic()
    
        
    
    def get_content(self):
        if self.language == "zh":
            message_template =[
                    {"role": "system", "content": f"你是一个观点鲜明的辩手，你需要根据接收到的命令选择明确地{self.stand}以下内容,值得注意的是，支持一个反对论述那么你的立场也是反对原论述，反对一个反对论述那么你的立场就应该变为支持原论述"},
                    {"role": "user", "content":""},
                              ]
        elif self.language == "en":
            message_template =[
                    {"role": "system", "content": f"You are a debater with a clear point of view. You need to choose to clearly {self.stand} the following content according to the commands you receive. It is worth noting that if you support an opposing argument, your position is also opposed to the original argument, and if you oppose an opposing argument, then Your position should change to support the original argument"},
                    {"role": "user", "content":""},
                              ]
        message_template[1]['content'] = self.target.content
        self.context = message_template
        answer = self.debater.invoke(message_template,self.round)
        self.content = answer
        pass
    
    

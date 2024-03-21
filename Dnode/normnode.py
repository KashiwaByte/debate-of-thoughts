#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 09:57:35
@File: Dnode\normnode.py
@IDE: vscode
@Description:
    基础类节点
"""

from .abnodes import AbNode
from Debater import D_Openai
class NormNode(AbNode):
    
    
    def __init__(self, round: int, out_node: AbNode, debater, standpoint: int):
        super().__init__(round, out_node, debater, standpoint)
    

    
    def get_topic(self):
        return super().get_topic()
    
    def get_stand(self):
        return super().get_stand()
        
    
    def get_content(self):
        message_template =[
                 {"role": "system", "content": f"你是一个观点鲜明的辩手，你需要根据接收到的命令选择明确地{self.stand}以下内容,值得注意的是，支持一个反对论述那么你的立场也是反对原论述，反对一个反对论述那么你的立场就应该变为支持原论述"},
                 {"role": "user", "content":""},
                            ]
        message_template[1]['content'] = self.target.content
        self.context = message_template
        answer = self.debater.invoke(message_template)
        self.content = answer
        pass
    
    
    def get_depth(self):
        return super().get_depth()
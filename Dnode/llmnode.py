#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 09:57:35
@File: Dnode\llmnode.py
@IDE: vscode
@Description:
    基础llm类节点
"""

from .abnode import AbNode
from Dagent import D_Openai
class LLMNode(AbNode):
    
    
    def __init__(self, round: int, out_node: AbNode,api,standpoint:int=-1):
        super().__init__(round, out_node,standpoint)
        self.debater=D_Openai(api_key=api)
        
    
    
    def get_stand(self):
        return super().get_stand()
        
    
    def get_content(self):
        message_template =[
                 {"role": "system", "content": f"你是一个观点鲜明的辩手，你需要根据接收到的命令选择明确地{self.stand}以下内容"},
                 {"role": "user", "content":""},
                            ]
        message_template[1]['content'] = self.target.content
        self.context = message_template
        answer = self.debater.invoke(message_template)
        self.content = answer
        pass
    
    
    def get_point(self):
        return super().get_point()
    
    
    
    def get_depth(self):
        return super().get_depth()
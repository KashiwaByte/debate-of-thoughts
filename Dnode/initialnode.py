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
from ..Dagent import D_Openai
class llmnode(AbNode):
    
    def __init__(self,topic):
        self.round_id = 1
        self.topic = topic
        D_Openai()
        
        
    def get_content(self):
        answer = D_Openai.invoke(self.topic)
        self.content = answer
       
    
    
    def get_point(self):
        return super().get_point()

    
    def get_depth(self):
        self.depth = 0
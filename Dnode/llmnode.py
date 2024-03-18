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
from ..Dagent import D_Openai
class llmnode(AbNode):
    
    def __init__(self, round: int, out_node: AbNode):
        super().__init__(round, out_node)
        D_Openai()
        
        
    def get_content(self):
        D_Openai.invoke(self.target.content)
        
        pass
    
    
    def get_point(self):
        return super().get_point()
    
    
    def get_depth(self, target):
        return super().get_depth(target)
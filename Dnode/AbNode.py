#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 16:11:06
@File: Dnode\AbNode.py
@IDE: vscode
@Description:
    抽象node类
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class AbNode(ABC):
    """  """
    
    
    
    def __init__(self,round:int,out_node:AbNode,debater,standpoint:int):
        self.round_id = round
        self.target = out_node
        self.debater=debater
        self.standpoint = standpoint
        self.get_depth()
        self.get_stand()
     #  self.get_content()
        pass
    

        
    
    def get_stand(self):
        if self.standpoint == 1:
            self.stand = "支持"
        elif self.standpoint == -1:
            self.stand = "反对"
        else: 
            print(f'standpoint只能输入1或者-1')

    
    @abstractmethod
    def get_content(self):
        '''最小闭环的get_content先做成指定使openai直接生成'''
        ''' self.content = func(out_node.content) '''

        pass
    
    
    def get_point(self):
        pass
    
    def get_depth(self):
        self.depth = self.target.depth + 1
        pass
    
    
    
    
    
    
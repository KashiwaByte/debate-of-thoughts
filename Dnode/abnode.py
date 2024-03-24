#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 16:11:06
@File: Dnode\abnode.py
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
    
    
    
    def __init__(self,round:int,out_node:AbNode,debater,standpoint:int,language:str = "zh"):
        self.round_id = round
        self.target = out_node
        self.debater=debater
        self.standpoint = standpoint
        self.language = language
        self.get_depth()
        self.get_stand()
        self.get_topic()
        self.get_content()
        pass
    

    def get_topic(self):
        self.topic = self.target.topic
    
    def get_stand(self):
        
        if self.language == "zh":
            if self.standpoint == 1:
                self.stand = "支持"
            elif self.standpoint == -1:
                self.stand = "反对"
            else: 
                print(f'standpoint只能输入1或者-1')
        elif self.language == 'en':
            if self.standpoint == 1:
                self.stand = "support"
            elif self.standpoint == -1:
                self.stand = "oppose"
            else: 
                print(f'standpoint can only be 1 or -1')
        else:
            print("当前只支持'zh'(中文）和'en'(英文)")

    
    @abstractmethod
    def get_content(self):
        '''最小闭环的get_content先做成指定使openai直接生成'''
        ''' self.content = func(out_node.content) '''

        pass
    
    
    def get_depth(self):
        self.depth = self.target.depth + 1
        pass
    
    
    
    
    
    
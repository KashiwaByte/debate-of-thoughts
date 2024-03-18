#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 08:45:37
@File: Dobserver\abobserver.py
@IDE: vscode
@Description:
    Observer抽象类
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class AbObserver(ABC):
    
    def __init__(self,name:str ,max_round:int = 5 ):
        self.round = 1 
        self.name = name
    
    def log(self):
        pass
    
    
    def update_round(self):
        '''全局round+1'''
        self.round+1
    

    
    def new_round(self):
        '''根据策略展开新一轮辩论'''
        pass
    
    
    def get_relation(self):
        '''获取当前节点间的支持反对关系，返回一个矩阵'''
        pass
    
    
    def get_point(self):
        '''获取当前各节点的分数'''
        pass
    
    
    def get_influence(self):
        '''获取当前各节点的影响力'''
        pass
        
    def get_depth(self):
        """获取当前各节点的深度"""
    
    
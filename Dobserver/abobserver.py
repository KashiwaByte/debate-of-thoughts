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
import numpy as np
from Dnode import AbNode,InitNode


class AbObserver(ABC):
    
    def __init__(self,name:str ,max_round:int = 5 ):
        self.round = 1 
        self.name = name
        self.relation = np.zeros([1],dtype=int)
        self.nodelist = list()
        self.depthdict = dict()
        self.pointdict = dict()
        self.influencedict = dict()
        self.debaterdict = dict()
    
    def init_node(self,node:InitNode):
        self.node = node
        self.nodedict.append({"round_id":node.round_id,"topic":node.topic,"depth":node.depth,"debater":node.debater,"content":node.content})
    
    def update_node(self,node:AbNode):
        """更改当前记录的node,j字典形式记录当前node信息到列表中"""
        self.node = node
        self.nodedict.append({"round_id":node.round_id,"depth":node.depth,"debater":node.debater,"standpoint":node.standpoint,"stand":node.stand,"target":node.target,"content":node.content})
        
    
    def log(self,node:AbNode):
        pass
    
    
    def update_round(self):
        '''全局round+1'''
        self.round+1
    

    
    def new_round(self):
        '''根据策略展开新一轮辩论,最小实现不做策略选择'''
        pass
    
    
    def update_relation(self):
        '''获取当前节点间的支持反对关系，返回一个矩阵'''
        self.relation = np.pad(self.relation, pad_width=((0, 1), (0, 1)), mode='constant')
        self.relation[self.round-1,self.node.target.round_id-1] = self.node.standpoint
        
    
    def update_depth(self):
        """获取当前各节点的深度，返回一个字典"""
        self.depthdict[f"node{self.round}":self.node.depth]

    
    def update_debater(self):
        self.debaterdict[f"node{self.round}":self.node.debater]
    
    def update_point(self):
        '''获取当前各节点的分数，返回一个字典'''
        pass
    
    
    def update_influence(self):
        '''获取当前各节点的影响力，返回一个字典'''
        pass
        
  
    
        
    
    
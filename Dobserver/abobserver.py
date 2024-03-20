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
from loguru import logger


import os
import sys
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建相对路径
relative_path = os.path.join(current_dir, '..')
# 将相对路径添加到sys.path
sys.path.append(relative_path)
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
        logger.add(f"logs/file_{self.name}.log", encoding="utf-8")
    
    def init_node(self,node:InitNode):
        self.node = node
        self.nodelist.append({"round_id":node.round_id,"node":node,"topic":node.topic,"depth":node.depth,"debater":node.debater,"content":node.content})
    
    def update_node(self,node:AbNode):
        """更改当前记录的node,j字典形式记录当前node信息到列表中"""
        self.node = node
        self.nodelist.append({"round_id":node.round_id,"node":node,"depth":node.depth,"debater":node.debater,"standpoint":node.standpoint,"stand":node.stand,"target":node.target,"content":node.content})
        
    
    def log(self):
        """记录当前轮次信息"""
        if self.round ==1:
            logger.info(
                    f'\n当前轮次为：{self.round}'
                    f'\n本轮节点使用的Debater为：{self.node.debater}'
                    f'\n本轮节点的{self.node.topic}论述是：{self.node.content}'
                    f'\n当前的关系矩阵为：\n{self.relation}'
                # f'\n当前各节点分数为：{self.point}'
                # f'\n当前各节点影响力为：{self.influence}'
                    )
        if self.round >1:
            logger.info(
                    f'\n当前轮次为：{self.round}'
                    f'\n本轮节点使用的Debater为：{self.node.debater}'
                    f'\n本轮节点 {self.node.stand} node_{self.node.target.round_id}'
                #   f'\n本轮节点的上文是：{self.node.context}'
                    f'\n本轮节点的{self.node.stand}论述是：{self.node.content}'
                    f'\n当前的关系矩阵为：\n{self.relation}'
                # f'\n当前各节点分数为：{self.point}'
                # f'\n当前各节点影响力为：{self.influence}'
                    )
        pass
    
    
    def update(self):
        self.update_relation()
        self.update_debater()
        self.update_depth()
        self.log()
        self.update_round()
    
    def update_round(self):
        '''全局round+1'''
        self.round +=1
    
    
    def update_relation(self):
        '''获取当前节点间的支持反对关系，返回一个矩阵'''
        if self.round == 2:
            self.relation = np.array([[0,0],[0,0]])
            self.relation[self.round-1,self.node.target.round_id-1] = self.node.standpoint
        if self.round > 2:
            self.relation = np.pad(self.relation, pad_width=((0, 1), (0, 1)), mode='constant')
            self.relation[self.round-1,self.node.target.round_id-1] = self.node.standpoint
        else:
            pass
    
    def update_depth(self):
        """获取当前各节点的深度，返回一个字典"""
        self.depthdict.update({f"node{self.round}":self.node.depth})

    
    def update_debater(self):
        self.debaterdict.update({f"node{self.round}":self.node.debater})
    
    def update_point(self):
        '''获取当前各节点的分数，返回一个字典'''
        pass
    
    
    def update_influence(self):
        '''获取当前各节点的影响力，返回一个字典'''
        pass
        
  
    
        
    
    
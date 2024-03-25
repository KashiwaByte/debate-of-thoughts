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
from Debater import AbDebater


class AbObserver(ABC):
    
    def __init__(self,name:str ,max_round:int = 5 ):
        self.round = 1 
        self.max_round =max_round
        self.name = name
        self.relation = np.zeros([1],dtype=int)
        self.nodelist = list()
        self.debaterlist = list()
        self.depthdict = dict()
        self.scoredict = dict()
        self.valscoredict = dict()
        self.influencedict = dict()
        self.debaterdict = dict()
        logger.add(f"logs/file_{self.name}.log", encoding="utf-8")
    
    def add_debater(self,debater:AbDebater,describe):
        """添加可用辩手到列表"""
        self.debaterlist.append({"describe":describe,"debater":debater})
    
    def init_node(self,node:InitNode):
        self.node = node
        self.nodelist.append({"round_id":node.round_id,"node":node,"topic":node.topic,"score":node.score,"depth":node.depth,"debater":node.debater,"content":node.content})
    
    def update_node(self,node:AbNode):
        """更改当前记录的node,j字典形式记录当前node信息到列表中"""
        self.node = node
        self.nodelist.append({"round_id":node.round_id,"node":node,"topic":node.topic,"score":node.score,"depth":node.depth,"debater":node.debater,"standpoint":node.standpoint,"stand":node.stand,"target":node.target,"content":node.content})
        
    
    def log(self):
        """记录当前轮次信息"""
        if self.round ==1:
            logger.info(
                    f'\n当前轮次为：{self.round}'
                    f'\n本轮节点使用的Debater为：{self.node.debater}'
                    f'\n本轮节点关于主题{self.node.topic}的论述是：{self.node.content}'
                    f'\n本轮节点的原始论证分数是{self.node.score}'
                    f'\n当前的关系矩阵为：\n{self.relation}'
                    f'\n当前各节点检证分数为：{self.valscoredict}'
                # f'\n当前各节点影响力为：{self.influence}'
                    )
        if self.round >1:
            logger.info(
                    f'\n当前轮次为：{self.round}'
                    f'\n本轮节点使用的Debater为：{self.node.debater}'
                    f'\n本轮节点 {self.node.stand} node_{self.node.target.round_id}'
                    f'\n本轮节点的上文是：{self.node.context}'
                    f'\n本轮节点的{self.node.stand}论述是：{self.node.content}'
                    f'\n本轮节点的原始论证分数是{self.node.score}'
                    f'\n当前的关系矩阵为：\n{self.relation}'
                    f'\n当前各节点检证分数为：{self.valscoredict}'
                # f'\n当前各节点影响力为：{self.influence}'
                    )
        
    
    
    def update(self):
        self.update_relation()
        self.update_debater()
        self.update_depth()
        self.update_score()
        self.update_validation_score()
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
        """获取当前各节点使用的辩手，返回一个字典"""
        self.debaterdict.update({f"node{self.round}":self.node.debater})
    
    def update_score(self):
        '''获取当前各节点的原始分数，返回一个字典'''
        self.scoredict.update({f"node{self.round}":self.node.score})
        
    def update_validation_score(self):
        '''获取当前各节点的检证后分数，返回一个字典'''
        # θ δ β λ是学习参数，θ是影响系数(0<α<1)，δ是深度系数(0<δ<1)受深度影响，β是检证系数（β>1)，λ是修正系数(0<γ<1)
        self.valscoredict = dict(self.scoredict)
        if self.round == 1:
            pass
        elif self.round > 1:
            for i in reversed(range(2,self.round+1)):
                θ = 0.5
                δ = 10/(9 + self.nodelist[i-1]["depth"])
                β = 1.2
                λ = 0.8
                standpoint = self.nodelist[i-1]["standpoint"]
                target_id = self.nodelist[i-1]["target"].round_id
                target_score = float(self.valscoredict[f"node{target_id}"])
                score = float(self.valscoredict[f"node{i}"])
             # 如果小于论证小于30分应该直接dropout
                if score>=30: 
                    if standpoint == -1:
                        target_val_score = (target_score+standpoint*θ*δ*score)*β
                    elif standpoint == 1:
                        target_val_score = (target_score+standpoint*θ*δ*score)*λ
                    self.valscoredict.update({f"node{target_id}":target_val_score}) 
                else:
                    pass
       
    
    def update_influence(self):
        '''获取当前各节点的影响力，返回一个字典'''
        pass
        
  
    
        
    
    
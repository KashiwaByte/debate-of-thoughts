#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-02 20:52:03
@File: Dobserver\ccacobserver.py
@IDE: vscode
@Description:
    用于CCAC智慧论辩测评的Observer类
"""
from __future__ import annotations
from loguru import logger


import os
import sys
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建相对路径
relative_path = os.path.join(current_dir, '..')
# 将相对路径添加到sys.path
sys.path.append(relative_path)
from Dnode import AbNode,InitNode,CCACNode
from Debater import AbDebater
from Dobserver import AbObserver


class CCACObserver(AbObserver):
    
    def __init__(self,name:str ,max_round:int = 6 ):
        self.round = 1 
        self.max_round =max_round
        self.name = name
        self.nodelist = list()
        self.debaterlist = list()
        self.scoredict = dict()
        self.debaterdict = dict()
        logger.add(f"logs/file_{self.name}.log", encoding="utf-8")
    
    def get_round_name(self):
        """用于获取该环节名称"""
        if self.round == 1:
            self.round_name = "正方立论"
        elif self.round == 2:
            self.round_name = "反方立论"
        elif self.round == 3:
            self.round_name = "正方驳论"
        elif self.round == 4:
            self.round_name = "反方驳论"
        elif self.round == 5:
            self.round_name = "正方结辩"
        elif self.round == 6:
            self.round_name = "反方结辩"
    
    def add_debater(self,debater:AbDebater,describe):
        """添加可用辩手到列表"""
        self.debaterlist.append({"describe":describe,"debater":debater})
    

    def update_node(self,node:AbNode):
        """更改当前记录的node,j字典形式记录当前node信息到列表中"""
        self.node = node
        self.nodelist.append({"round":node.round,"node":node,"score":node.score,"content":node.content})
        
    
    def log(self):
        """记录当前轮次信息"""
        if self.round ==1:
            logger.info(
                    f'\n当前环节为：{self.round_name}'
                    f'\n本环节使用的Debater为：{self.node.debater}'
                    f'\n本环节的论述是：{self.node.content}'
                    f'\n本环节的原始论证分数是{self.node.score}'
                    )
        if self.round >1:
            logger.info(
                    f'\n当前环节为：{self.round_name}'
                    f'\n本环节使用的Debater为：{self.node.debater}'
                    f'\n本环节的论述是：{self.node.content}'
                    f'\n本环节的原始论证分数是{self.node.score}'
                    )
        
    
    
    def update(self):
        self.get_round_name()
        self.update_debater()
        self.update_score()
        self.log()
        self.update_round()
    
    def update_round(self):
        '''全局round+1'''
        self.round +=1
    

    def update_debater(self):
        """获取当前各节点使用的辩手，返回一个字典"""
        self.debaterdict.update({f"node{self.round}":self.node.debater})
    
    def update_score(self):
        '''获取当前各节点的原始分数，返回一个字典'''
        self.scoredict.update({f"node{self.round}":self.node.score})
        
    
       
    

  
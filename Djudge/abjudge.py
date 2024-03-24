#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 12:59:40
@File: Djudge\abjudge.py
@IDE: vscode
@Description:
    抽象judge基类
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '..')
sys.path.append(relative_path)
from Debater import D_Openai
from Dnode import AbNode,InitNode,NormNode
from Dobserver import AbObserver
import random
from debater_python_api.api.debater_api import DebaterApi
class AbJudge(ABC):
    
    def __init__(self,observer:AbObserver,debaterapi:str,language:str = 'zh'):
        self.observer = observer
        self.language = language
        debater_api = DebaterApi(debaterapi)
        self.argument_quality_client = debater_api.get_argument_quality_client()
        
    
    
    def new_node(self):
        new_round = self.observer.round
        new_outnode = self.get_outnode()       #后续根据算法得出
        new_debater = self.get_debater()  #后续根据算法得出
        new_standpoint = self.get_standpoint()                 #后续根据算法得出
        
        node  = NormNode(round=new_round, out_node=new_outnode, debater=new_debater , standpoint=new_standpoint,language=self.language)
        node.point = self.get_point(node)
        return node
        
    
    
    def get_point(self,node:AbNode):
        """新节点获取分数的方法"""
        topic = node.topic
        sentence = node.content
        sentence_topic_dict = [{'sentence':sentence,'topic':topic}]
        scores = self.argument_quality_client.run(sentence_topic_dict)
        return scores
        
    
    
    def get_outnode(self):
        """新节点获取目标节点的方法"""
        i = self.observer.round
        n = random.randint(1,i-1)
        return  self.observer.nodelist[n-1]["node"]
        
        
        
        
    def get_debater(self):
        """新节点获取辩手的方法"""
        return self.observer.nodelist[0]["debater"]
        
        
    def get_standpoint(self):
        """新节点获取论述意向的方法"""
        return random.choice([-1,1])
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
import SparkApi
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
        node.score = self.get_score(node)
        return node
        
    
    
    def get_score(self,node:AbNode):
        """新节点获取分数的方法"""
        topic = node.topic
        sentence = node.content
        if self.language=="zh":
            text =[ {"role": "system",
                     "content": "请根据以下论述和主题,给出论证质量评分(只需要输出一个范围从0-1的分数,精确到小数点后9位),不要给出分析."},
                    { "role":"user",
                      "content":str({'sentence':sentence , 'topic': topic})          
                         }]
            SparkApi.main(text)
            scores = SparkApi.answer
        elif self.language=="en":
            sentence_topic_dict = [{'sentence':sentence,'topic':topic}]
            scores = self.argument_quality_client.run(sentence_topic_dict)
        score = format(scores[0]*100, '.3f')
        return score
        
    
    
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
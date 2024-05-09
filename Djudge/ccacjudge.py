#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-02 19:41:22
@File: Djudge\CCACjudge.py
@IDE: vscode
@Description:
    用于CCAC智慧论辩测评
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '..')
sys.path.append(relative_path)
from Djudge import AbJudge
from Dnode import AbNode,CCACNode
from Dobserver import AbObserver
from Djudge import SparkApi

class CCACJudge(AbJudge):
    """用于CCAC测评,主要针对得分和流程进行定制"""
    
    def __init__(self,topic,observer:AbObserver,language:str = 'zh'):
        self.topic = topic
        self.observer = observer
        self.language = language

        
    
    
    def new_node(self,context):
        new_round = self.observer.round
        new_debater = self.get_debater()  #后续根据算法得出
        
        node  = CCACNode(round=new_round,debater=new_debater,topic=self.topic,context=context,language=self.language)
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
        score = format(float(scores[0])*100, '.3f')
        return score
        
    
    
    def get_outnode(self):
        """新节点获取目标节点的方法"""
        i = self.observer.round 
        n = i-1
        return  self.observer.nodelist[n-1]["node"]
        
        
        
        
    def get_debater(self):
        """新节点获取辩手的方法"""
        i = self.observer.round 
        if i%2 == 1:
            return self.observer.debaterlist[0]["debater"]
        if i%2 == 0:
            return self.observer.debaterlist[1]["debater"]


if __name__ == "__main__":
    print("1")
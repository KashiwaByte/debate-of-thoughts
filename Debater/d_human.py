#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-26 15:33:16
@File: Debater\d_human.py
@IDE: vscode
@Description:
    人类输入辩手
"""

from .abdebater import AbDebater

class D_Human(AbDebater):
    
    def __init__(self, model: str='human'):
        super().__init__(model)
        
        
    def response(self, message):
        pass
    
    def invoke(self,message):
        answer = input(message)
        return answer
        
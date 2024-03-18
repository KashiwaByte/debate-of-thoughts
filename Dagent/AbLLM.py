#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 08:46:59
@File: Dagent\AbLLM.py
@IDE: vscode
@Description:
    大模型抽象类
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class AbLLM(ABC):
    
    def __init__(self,model:str,):
        self.model = model
        pass
    
    @abstractmethod
    def response(self,message):
        pass
    
    @abstractmethod
    def invoke():
        pass
    
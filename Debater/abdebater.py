#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 21:33:45
@File: Debater\abdebater.py
@IDE: vscode
@Description:
    抽象debater类
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class AbDebater(ABC):
    
    def __init__(self,model:str,):
        self.model = model
        pass
    
    @abstractmethod
    def response(self,message):
        pass
    
    @abstractmethod
    def invoke():
        pass
    
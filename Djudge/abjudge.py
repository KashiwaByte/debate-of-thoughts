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


class AbJudge(ABC):
    
    def __init__(self):
        pass
    
    
    def new_round(self):
        pass
        
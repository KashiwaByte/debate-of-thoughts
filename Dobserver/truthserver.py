#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-18 16:14:15
@File: Dobserver\truthserver.py
@IDE: vscode
@Description:
    事实类observer
"""

from .abobserver import AbObserver

class TruthObserver(AbObserver):
    
    def __init__(self, name: str, max_round: int = 5):
        super().__init__(name, max_round)
        
        
    
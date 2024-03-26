#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-26 17:45:15
@File: Dtest\d_human.py
@IDE: vscode
@Description:
    人类辩手脚本
"""

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '..')
sys.path.append(relative_path)
from Dnode import InitNode,NormNode
from Dobserver import AbObserver
from Debater import D_Human
from Djudge import AbJudge
from Dgraph import upload

human_debater = D_Human(model="kashiwa")

message_template =[
                    {"role": "system", "content": f"你是一个观点鲜明的辩手，你需要根据接收到的命令选择明确地支持以下内容,值得注意的是，支持一个反对论述那么你的立场也是反对原论述，反对一个反对论述那么你的立场就应该变为支持原论述"},
                    {"role": "user", "content":"今天星期几？"},
                              ]

human_debater.invoke(f'{message_template} 请输入你的答案：')
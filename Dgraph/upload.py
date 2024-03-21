#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-03-21 21:37:27
@File: Dgraph\upload.py
@IDE: vscode
@Description:
    数据上传Neo4j函数
"""
from py2neo import Graph, Node, Relationship

# 建立一个Neo4j会话


def node_upload(max_round,node_list):
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "NEO123456neo"))
    var = "upload"
    node_name = f'{var}1' 
    globals()[node_name] = Node("round",**node_list[0])
 
    for i in (2,max_round+1):
        node_name = f'{var}{i}' 
        globals()[node_name] = Node("round",**node_list[i-1])
        relationship = Relationship(globals()[node_name],node_list[i-1]["stand"],globals()[f'upload{globals()[node_name]["target"].round_id}'])
        graph.create(relationship)

 
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
    """传入的node_list的修改target类型后上传到图数据库"""
    node_lists =  node_list
    print(f"初始{node_lists}")
    
    for i in range(0,max_round):
        """从第一项遍历到最后一项"""
        node_lists[i]["node"] = f'graphnode{node_lists[i]["round_id"]}'
        node_lists[i]["debater"] = f'{node_lists[i]["debater"].__class__}'
    
    for i in range(1,max_round):
        """从第二项遍历到最后一项"""
        node_lists[i]["target"] = f'graphnode{node_lists[i]["target"].round_id}'
    print(f"修改后:{node_lists}")
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "NEO123456neo"))
    var = "graphnode"
    node_name = f'{var}1' 
    globals()[node_name] = Node("round",**node_lists[0])
 
    for i in range(2,max_round+1):
        node_name = f'{var}{i}' 
        globals()[node_name] = Node("round",**node_list[i-1])
        relationship = Relationship(globals()[node_name],node_lists[i-1]["stand"],globals()[f'{globals()[node_name]["target"]}'])
        graph.create(relationship)

 
 
 
 
 
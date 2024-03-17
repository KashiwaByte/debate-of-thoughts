from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class AbNode(ABC):
    """  """
    
    
    
    def __init__(self,round:int,out_node:AbNode):
        self.round_id = round
        self.target = out_node
        pass
        
        
    
    
    @abstractmethod
    def get_content(self,out_node):
        ''' self.content = func(out_node.content) '''
       
        pass
    
    
    def get_point(self):
        pass
    
    def get_depth(self,target):
        self.depth = target.depth + 1
        pass
    
    
    
    
    
    
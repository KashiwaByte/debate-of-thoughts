from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class AbObserver(ABC):
    
    def __init__(self,max_round:int):
        self.round = 1 
    
    def log(self):
        pass
    
    
    def update_round(self):
        self.round+1
    
    def new_round(self):
        pass
    
    
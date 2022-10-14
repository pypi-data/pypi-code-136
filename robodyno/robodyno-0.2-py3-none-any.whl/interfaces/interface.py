#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""interface.py
Time    :   2022/09/30
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Robodyno Interface Abstract Class
"""

from abc import ABC, abstractmethod

class Interface(ABC):
    """Interface with get node methods."""
    
    @abstractmethod
    def get_motor_node(self, motor):
        """Get motor node from current interface.
        
        Args:
            motor: robodyno motor object
        
        Returns:
            motor node with specific interface
        """

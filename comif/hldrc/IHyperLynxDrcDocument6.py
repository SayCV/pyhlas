# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-12:11:09
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IHyperLynxDrcDocument6(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def BondWires(self):
        return self.obj.BondWires

    @property
    def BondFingers(self):
        return self.obj.BondFingers

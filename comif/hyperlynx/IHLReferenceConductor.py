# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-20:13:09
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IHLReferenceConductor(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Layer(self):
        return self.obj.Layer

    @property
    def Pos(self):
        return self.obj.Pos

    @property
    def Width(self):
        return self.obj.Width

    @property
    def Type(self):
        return self.obj.Type


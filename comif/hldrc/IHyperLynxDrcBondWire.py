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

class IHyperLynxDrcBondWire(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Diameter(self):
        return self.obj.Diameter

    @property
    def Length(self):
        return self.obj.Length

    @property
    def IsConnected(self):
        return self.obj.IsConnected

    @property
    def Points(self):
        return self.obj.Points

    @property
    def Height(self):
        return self.obj.Height

    @property
    def Net(self):
        return self.obj.Net


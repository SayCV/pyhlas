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

class IHLScmVoltage(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def SupplyNet(self):
        return self.obj.SupplyNet

    @SupplyNet.setter
    def SupplyNet(self, SupplyNet):
        self.obj.SupplyNet=SupplyNet


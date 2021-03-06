# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-11:53:05
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IPowerLogicMeasure(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Value(self):
        return self.obj.Value

    @Value.setter
    def Value(self, Value):
        self.obj.Value=Value

    @property
    def Text(self):
        return self.obj.Text

    @property
    def Name(self):
        return self.obj.Name

    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def unit(self):
        return self.obj.unit

    @property
    def Prefix(self):
        return self.obj.Prefix

    @property
    def Number(self):
        return self.obj.Number

    @property
    def Normalize(self):
        return self.obj.Normalize

    @Text.setter
    def Text(self, Text):
        self.obj.Text=Text


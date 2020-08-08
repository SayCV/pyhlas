# coding=utf-8
"""
This file is autogenerated by python script @ 20200726-10:57:03
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IPowerPCBLabel(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def Name(self):
        return self.obj.Name

    @property
    def LabelType(self):
        return self.obj.LabelType

    @property
    def Display(self):
        return self.obj.Display

    @property
    def Application(self):
        return self.obj.Application

    @property
    def Component(self):
        return self.obj.Component

    @property
    def Attribute(self):
        return self.obj.Attribute

    @property
    def RightReading(self):
        return self.obj.RightReading

    @Display.setter
    def Display(self, Display):
        self.obj.Display=Display

    @property
    def selected(self):
        return self.obj.selected

    @RightReading.setter
    def RightReading(self, RightReading):
        self.obj.RightReading=RightReading

    @property
    def Text(self):
        return self.obj.Text

    @property
    def Delete(self):
        return self.obj.Delete

    @selected.setter
    def selected(self, selected):
        self.obj.selected=selected

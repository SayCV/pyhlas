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

class IPowerPCBPartType(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def Name(self):
        return self.obj.Name

    @property
    def selected(self):
        return self.obj.selected

    @property
    def Components(self):
        return self.obj.Components

    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def Logic(self):
        return self.obj.Logic

    @selected.setter
    def selected(self, selected):
        self.obj.selected=selected

    @property
    def ECORegistered(self):
        return self.obj.ECORegistered

    @property
    def TimeStamp(self):
        return self.obj.TimeStamp

    @property
    def LibraryTimeStamp(self):
        return self.obj.LibraryTimeStamp

    @ECORegistered.setter
    def ECORegistered(self, ECORegistered):
        self.obj.ECORegistered=ECORegistered

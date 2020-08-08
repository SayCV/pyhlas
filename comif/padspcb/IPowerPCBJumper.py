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

class IPowerPCBJumper(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def Orientation(self):
        return self.obj.Orientation

    @property
    def points(self):
        return self.obj.points

    @property
    def selected(self):
        return self.obj.selected

    @property
    def Name(self):
        return self.obj.Name

    @property
    def Net(self):
        return self.obj.Net

    @property
    def Length(self):
        return self.obj.Length

    @selected.setter
    def selected(self, selected):
        self.obj.selected=selected

    @property
    def Installed(self):
        return self.obj.Installed

    @Installed.setter
    def Installed(self, Installed):
        self.obj.Installed=Installed

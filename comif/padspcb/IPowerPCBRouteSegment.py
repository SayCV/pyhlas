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

class IPowerPCBRouteSegment(object):
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
    def Net(self):
        return self.obj.Net

    @property
    def layer(self):
        return self.obj.layer

    @property
    def width(self):
        return self.obj.width

    @property
    def Name(self):
        return self.obj.Name

    @property
    def selected(self):
        return self.obj.selected

    @property
    def SegmentType(self):
        return self.obj.SegmentType

    @property
    def Length(self):
        return self.obj.Length

    @property
    def points(self):
        return self.obj.points

    @property
    def Protected(self):
        return self.obj.Protected

    @selected.setter
    def selected(self, selected):
        self.obj.selected=selected


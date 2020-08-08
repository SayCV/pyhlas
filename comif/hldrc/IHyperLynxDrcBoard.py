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

class IHyperLynxDrcBoard(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def OriginX(self):
        return self.obj.OriginX

    @property
    def OriginY(self):
        return self.obj.OriginY

    @property
    def TopLayerIndex(self):
        return self.obj.TopLayerIndex

    @property
    def Outline(self):
        return self.obj.Outline

    @property
    def Components(self):
        return self.obj.Components

    @property
    def Nets(self):
        return self.obj.Nets

    @property
    def NetClasses(self):
        return self.obj.NetClasses

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Vias(self):
        return self.obj.Vias

    @property
    def LayerStackups(self):
        return self.obj.LayerStackups

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def ObjectsInShape(self):
        return self.obj.ObjectsInShape

    @property
    def FullName(self):
        return self.obj.FullName

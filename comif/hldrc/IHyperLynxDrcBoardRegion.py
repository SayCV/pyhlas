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

class IHyperLynxDrcBoardRegion(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def LayerStackup(self):
        return self.obj.LayerStackup

    @property
    def BendAreas(self):
        return self.obj.BendAreas

    @property
    def Type(self):
        return self.obj.Type

    @property
    def AreaFills(self):
        return self.obj.AreaFills

    @property
    def Components(self):
        return self.obj.Components

    @property
    def Traces(self):
        return self.obj.Traces

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Vias(self):
        return self.obj.Vias

    @property
    def MountingHoles(self):
        return self.obj.MountingHoles

    @property
    def BondFingers(self):
        return self.obj.BondFingers

    @property
    def Fiducials(self):
        return self.obj.Fiducials

    @property
    def SubRegions(self):
        return self.obj.SubRegions

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def Outline(self):
        return self.obj.Outline

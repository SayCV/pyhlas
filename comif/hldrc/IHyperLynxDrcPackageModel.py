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

class IHyperLynxDrcPackageModel(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Thickness(self):
        return self.obj.Thickness

    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def HeatsinkWidth(self):
        return self.obj.HeatsinkWidth

    @Thickness.setter
    def Thickness(self, Thickness):
        self.obj.Thickness=Thickness

    @property
    def HeatsinkLength(self):
        return self.obj.HeatsinkLength

    @HeatsinkWidth.setter
    def HeatsinkWidth(self, HeatsinkWidth):
        self.obj.HeatsinkWidth=HeatsinkWidth

    @property
    def HeatsinkThickness(self):
        return self.obj.HeatsinkThickness

    @HeatsinkLength.setter
    def HeatsinkLength(self, HeatsinkLength):
        self.obj.HeatsinkLength=HeatsinkLength

    @property
    def HasHeatSink(self):
        return self.obj.HasHeatSink

    @HeatsinkThickness.setter
    def HeatsinkThickness(self, HeatsinkThickness):
        self.obj.HeatsinkThickness=HeatsinkThickness

    @property
    def PinModels(self):
        return self.obj.PinModels

    @property
    def AddAttribute(self):
        return self.obj.AddAttribute

    @property
    def Delete(self):
        return self.obj.Delete

    @property
    def NewPackagePinModel(self):
        return self.obj.NewPackagePinModel

    @property
    def SetName(self):
        return self.obj.SetName

    @HasHeatSink.setter
    def HasHeatSink(self, HasHeatSink):
        self.obj.HasHeatSink=HasHeatSink


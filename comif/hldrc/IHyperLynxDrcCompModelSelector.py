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

class IHyperLynxDrcCompModelSelector(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def SelectedDeviceModel(self):
        return self.obj.SelectedDeviceModel

    @property
    def AvailableDeviceModels(self):
        return self.obj.AvailableDeviceModels

    @property
    def Component(self):
        return self.obj.Component

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def GetComment(self):
        return self.obj.GetComment

    @SelectedDeviceModel.setter
    def SelectedDeviceModel(self, SelectedDeviceModel):
        self.obj.SelectedDeviceModel=SelectedDeviceModel


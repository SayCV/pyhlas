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

class IHLLayer(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Name(self):
        return self.obj.Name

    @property
    def Type(self):
        return self.obj.Type

    @property
    def Thickness(self):
        return self.obj.Thickness

    @Name.setter
    def Name(self, Name):
        self.obj.Name=Name

    @property
    def Plating(self):
        return self.obj.Plating

    @Thickness.setter
    def Thickness(self, Thickness):
        self.obj.Thickness=Thickness

    @property
    def IsVisible(self):
        return self.obj.IsVisible

    @Plating.setter
    def Plating(self, Plating):
        self.obj.Plating=Plating

    @property
    def Color(self):
        return self.obj.Color

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self.obj.IsVisible=IsVisible

    @property
    def DrawStyle(self):
        return self.obj.DrawStyle

    @Color.setter
    def Color(self, Color):
        self.obj.Color=Color

    @property
    def Material(self):
        return self.obj.Material

    @DrawStyle.setter
    def DrawStyle(self, DrawStyle):
        self.obj.DrawStyle=DrawStyle

    @property
    def Fabrication(self):
        return self.obj.Fabrication

    @Material.setter
    def Material(self, Material):
        self.obj.Material=Material

    @property
    def Copy(self):
        return self.obj.Copy

    @Fabrication.setter
    def Fabrication(self, Fabrication):
        self.obj.Fabrication=Fabrication

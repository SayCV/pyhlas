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

class IHyperLynxDrcGeomEngine(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ParallelismTolerance(self):
        return self.obj.ParallelismTolerance

    @property
    def And(self):
        return self.obj.And

    @property
    def Or(self):
        return self.obj.Or

    @property
    def Xor(self):
        return self.obj.Xor

    @property
    def Distance(self):
        return self.obj.Distance

    @property
    def Angle(self):
        return self.obj.Angle

    @property
    def Parallel(self):
        return self.obj.Parallel

    @property
    def IsPointInsideShape(self):
        return self.obj.IsPointInsideShape

    @property
    def IsShapeInsideShape(self):
        return self.obj.IsShapeInsideShape

    @property
    def Overlap(self):
        return self.obj.Overlap

    @property
    def IsInTouch(self):
        return self.obj.IsInTouch

    @property
    def LateralOverlap(self):
        return self.obj.LateralOverlap

    @property
    def Expand(self):
        return self.obj.Expand

    @property
    def Inverse(self):
        return self.obj.Inverse

    @property
    def Subtract(self):
        return self.obj.Subtract

    @property
    def Cross(self):
        return self.obj.Cross

    @property
    def Rotate(self):
        return self.obj.Rotate

    @ParallelismTolerance.setter
    def ParallelismTolerance(self, ParallelismTolerance):
        self.obj.ParallelismTolerance=ParallelismTolerance

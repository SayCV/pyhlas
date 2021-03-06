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

class IHLSimStimulus(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def LoadJitter(self):
        return self.obj.LoadJitter

    @property
    def BitSequenceType(self):
        return self.obj.BitSequenceType

    @property
    def Jitter(self):
        return self.obj.Jitter

    @property
    def BitOrder(self):
        return self.obj.BitOrder

    @BitSequenceType.setter
    def BitSequenceType(self, BitSequenceType):
        self.obj.BitSequenceType=BitSequenceType

    @property
    def InitialState(self):
        return self.obj.InitialState

    @BitOrder.setter
    def BitOrder(self, BitOrder):
        self.obj.BitOrder=BitOrder

    @property
    def Frequency(self):
        return self.obj.Frequency

    @InitialState.setter
    def InitialState(self, InitialState):
        self.obj.InitialState=InitialState

    @property
    def DutyCycle(self):
        return self.obj.DutyCycle

    @Frequency.setter
    def Frequency(self, Frequency):
        self.obj.Frequency=Frequency

    @property
    def Repetitions(self):
        return self.obj.Repetitions

    @DutyCycle.setter
    def DutyCycle(self, DutyCycle):
        self.obj.DutyCycle=DutyCycle

    @Repetitions.setter
    def Repetitions(self, Repetitions):
        self.obj.Repetitions=Repetitions


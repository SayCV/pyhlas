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

class IHyperLynxDrcViolationType(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def HtmlHdr(self):
        return self.obj.HtmlHdr

    @property
    def HtmlBody(self):
        return self.obj.HtmlBody

    @HtmlHdr.setter
    def HtmlHdr(self, HtmlHdr):
        self.obj.HtmlHdr=HtmlHdr

    @property
    def HtmlFile(self):
        return self.obj.HtmlFile

    @HtmlBody.setter
    def HtmlBody(self, HtmlBody):
        self.obj.HtmlBody=HtmlBody

    @property
    def IdTemplate(self):
        return self.obj.IdTemplate

    @HtmlFile.setter
    def HtmlFile(self, HtmlFile):
        self.obj.HtmlFile=HtmlFile

    @property
    def VisibleProperties(self):
        return self.obj.VisibleProperties

    @IdTemplate.setter
    def IdTemplate(self, IdTemplate):
        self.obj.IdTemplate=IdTemplate

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def CommitRequired(self):
        return self.obj.CommitRequired

    @VisibleProperties.setter
    def VisibleProperties(self, VisibleProperties):
        self.obj.VisibleProperties=VisibleProperties

    @property
    def NewViolation(self):
        return self.obj.NewViolation

    @property
    def AddAttribute(self):
        return self.obj.AddAttribute

    @property
    def Delete(self):
        return self.obj.Delete

    @property
    def DefineAttribute(self):
        return self.obj.DefineAttribute

    @property
    def SetName(self):
        return self.obj.SetName

    @CommitRequired.setter
    def CommitRequired(self, CommitRequired):
        self.obj.CommitRequired=CommitRequired

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

class IHyperLynxDrcGraphEngine(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ShortestPathAlgorithm(self):
        return self.obj.ShortestPathAlgorithm

    @property
    def BreadthFirstSearch(self):
        return self.obj.BreadthFirstSearch

    @property
    def DepthFirstSearch(self):
        return self.obj.DepthFirstSearch

    @property
    def FindShortestPath(self):
        return self.obj.FindShortestPath

    @property
    def BuildTopologicalGraph(self):
        return self.obj.BuildTopologicalGraph

    @property
    def GetGraphComponents(self):
        return self.obj.GetGraphComponents

    @ShortestPathAlgorithm.setter
    def ShortestPathAlgorithm(self, ShortestPathAlgorithm):
        self.obj.ShortestPathAlgorithm=ShortestPathAlgorithm

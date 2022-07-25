# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:40:43 2022

离子强度（ionic strength）I等于溶液中每种离子i的质量摩尔浓度（mi）乘以该离子的价数（zi）的平方所得诸项之和得一半.

计算简单离子强度
"""

from chempy.electrolytes import ionic_strength
print(ionic_strength({'Fe+3':0.050,'ClO4-':0.150})==.3)

# True
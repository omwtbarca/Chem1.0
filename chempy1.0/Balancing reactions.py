# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 07:42:16 2022

Balancing reactions
redox——氧化还原
coefficient ——系数
"""
from chempy import Equilibrium
from sympy import symbols
K1,K2,Kw=symbols('K1 K2 Kw')
e1=Equilibrium({'MnO4-':1,'H+':8,'e-':5}, {'Mn+2':1,'H2O':4},K1)
e2=Equilibrium({'O2':1,'H2O':2,'e-':4}, {'OH-':4},K2)
coeff=Equilibrium.eliminate([e1,e2], 'e-')
print(coeff)
# [4, -5]
redox=e1*coeff[0]+e2*coeff[1]
print(redox)
#32 H+ + 4 MnO4- + 20 OH- = 26 H2O + 4 Mn+2 + 5 O2; K1**4/K2**5

autoprot=Equilibrium({'H2O':1}, {'H+':1,'OH-':1},Kw)
n=redox.cancel(autoprot)
print(n)
# 20

redox2=redox+n*autoprot
print(redox2)

# 12 H+ + 4 MnO4- = 6 H2O + 4 Mn+2 + 5 O2; K1**4*Kw**20/K2**5
'''
[4, -5]
32 H+ + 4 MnO4- + 20 OH- = 26 H2O + 4 Mn+2 + 5 O2; K1**4/K2**5
20
12 H+ + 4 MnO4- = 6 H2O + 4 Mn+2 + 5 O2; K1**4*Kw**20/K2**5
'''

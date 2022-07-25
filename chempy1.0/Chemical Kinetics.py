# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:42:40 2022

Chemical Kinetics ()
"""

#!pip install chempy
from chempy import ReactionSystem
rsys = ReactionSystem.from_string('\n'.join(['2 Fe+2 + H2O2 -> 2 Fe+3 + 2 OH-;42',
'2 Fe+3 + H2O2 -> 2 Fe+2 + O2 + 2 H+;17 ',
'H+ + OH- -> H2O; 1e10',

'H2O ->H+ + OH- ;1e-4',
'Fe+3 + 2 H2O ->FeOOH(s) + 3 H+;1',

'FeOOH(s)+ 3 H+ -> Fe+3 + 2 H2O; 2.5']))
from chempy.kinetics.ode import get_odesys
odesys,extra = get_odesys(rsys)
from collections import defaultdict
import numpy as np
tout = sorted(np.concatenate((np.linspace(0,23),np.logspace(-8,1))))
c0=defaultdict(float,{'Fe+2':0.05,'H2O2':0.1,'H2O':1.0,'H+':1e-7,'OH-':1e-7})
result = odesys.integrate(tout,c0,atol=1e-12,rtol=1e-14)

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
result.plot(names=[k for k in rsys.substances if k !='H2O'])
plt.legend(loc='best',prop={'size':9});_=plt.xlabel('Time');_=plt.ylabel('Concentration')
plt.subplot(1,2,2)
result.plot(names= [k for k in rsys.substances if k !='H2O'],xscale='log',yscale='log')
plt.legend(loc='best',prop={'size':9});_=plt.xlabel('Time');_=plt.ylabel('Concentration')
plt.tight_layout()
plt.show()
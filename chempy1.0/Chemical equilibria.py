# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:37:56 2022

Chemical equilibria
"""
from chempy import Equilibrium
from chempy.chemistry import Species 
water_autop = Equilibrium({'H2O'},{'H+','OH-'},10**-14)
ammonia_prot = Equilibrium({'NH4+'}, {'NH3','H+'},10**-9.24)
from chemical.equilibria import EqSystem
substances = map(Species.from_formula,'H2O OH- H+ NH3 NH4+'.split())
eqsys=EqSystem([water_autop,ammonia_prot].substances)
print('\n'.join(map(str,eqsys.rxns)))
'''

'''


from collections import defaultdict
init_conc=defaultdict(float,{'H2O':1,'NH3':0.1})
x,sol,sane=eqsys.root(init_conc)
assert sol['success'] and sane
print (sorted (sol.keys()))

print(','.join('%.2g'% v for v in x ))
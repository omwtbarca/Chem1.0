# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 07:31:49 2022

Balancing stoichiometry of a chmical reaction
"""

'''
* 反应配平！
Definition : balance_stoichiometry(reactants, products, substances=None,
           substance_factory=Substance.from_formula, parametric_symbols=None, 
           underdetermined=True, allow_duplicates=False)
'''

from chempy import  balance_stoichiometry  # main reaction in NASA's booster rockets:
reac , prod= balance_stoichiometry({'NH4ClO4','Al'},{'Al2O3','HCl','H2O','N2'})
from pprint import pprint
pprint(reac)
# OrderedDict([('Al', 10), ('NH4ClO4', 6)])
pprint(prod)
#OrderedDict([('Al2O3', 5), ('H2O', 9), ('HCl', 6), ('N2', 3)])


from chempy import mass_fractions
for fractions in map(mass_fractions,[reac,prod]):
    pprint({k:'{0:.3g}wt%'.format(v*100)for k,v in fractions.items()})
    
    '''
    
{'Al': '27.7wt%', 'NH4ClO4': '72.3wt%'}
{'Al2O3': '52.3wt%', 'H2O': '16.6wt%', 'HCl': '22.4wt%', 'N2': '8.62wt%'}
'''
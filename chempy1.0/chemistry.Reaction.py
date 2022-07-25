# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 07:27:14 2022

chemistry.Reaction
"""


# importing the module
from chempy import chemistry
 
# creating the reaction
reaction = chemistry.Reaction({'H2': 2, 'O2': 1},
                              {'H2O': 2})
 
# displaying the reaction
print(reaction)
 
# displaying the reaction order
print(reaction.order())


'''
2 H2 + O2 -> 2 H2O
3
'''
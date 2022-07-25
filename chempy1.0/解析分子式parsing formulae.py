
#Created on Fri Jul 22 07:21:27 2022
# Parsing formulae

from chempy import Substance
ferricyanide=Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition=={0:-3,26:1,6:6,7:6}
#True
print(ferricyanide.unicode_name)

print(ferricyanide.latex_name+","+ferricyanide.html_name)

print('%.9f' % ferricyanide.mass)
print(ferricyanide.charge)

'''
Fe(CN)₆³⁻
Fe(CN)_{6}^{3-},Fe(CN)<sub>6</sub><sup>3-</sup>
211.954646700
-3
'''
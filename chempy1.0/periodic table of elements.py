# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 07:26:04 2022

print elements table
periodic table of elements
"""

# importing the module
from chempy.util import periodic
 
# number of elements to be fetched
n = 117
 
# displaying the information
print("Atomic No.\tName\t\tSymbol\t\tMass")
 
# fetching the information for
# the first 10 elements
for i in range(1, n + 1):
 
    # displaying the atomic number
    print(i, end = "\t\t")
 
    # displaying the name
    if len(periodic.names[i]) > 7:
        print(periodic.names[i], end = "\t")
    else:
        print(periodic.names[i], end = "\t\t")
 
    # displaying the symbol
    print(periodic.symbols[i], end = "\t\t")
 
    # displaying the mass
    print(periodic.relative_atomic_masses[i])
    
    '''
    Atomic No.	Name		Symbol		Mass
1		Helium		He		4.002602
2		Lithium		Li		6.94
3		Beryllium	Be		9.0121831
4		Boron		B		10.81
5		Carbon		C		12.011
6		Nitrogen	N		14.007
7		Oxygen		O		15.999
8		Fluorine	F		18.998403163
9		Neon		Ne		20.1797
10		Sodium		Na		22.98976928
11		Magnesium	Mg		24.305
12		Aluminium	Al		26.9815385
13		Silicon		Si		28.085
14		Phosphorus	P		30.973761998
15		Sulfur		S		32.06
16		Chlorine	Cl		35.45
17		Argon		Ar		39.948
18		Potassium	K		39.0983
19		Calcium		Ca		40.078
20		Scandium	Sc		44.955908
21		Titanium	Ti		47.867
22		Vanadium	V		50.9415
23		Chromium	Cr		51.9961
24		Manganese	Mn		54.938044
25		Iron		Fe		55.845
26		Cobalt		Co		58.933194
27		Nickel		Ni		58.6934
28		Copper		Cu		63.546
29		Zinc		Zn		65.38
30		Gallium		Ga		69.723
31		Germanium	Ge		72.63
32		Arsenic		As		74.921595
33		Selenium	Se		78.971
34		Bromine		Br		79.904
35		Krypton		Kr		83.798
36		Rubidium	Rb		85.4678
37		Strontium	Sr		87.62
38		Yttrium		Y		88.90584
39		Zirconium	Zr		91.224
40		Niobium		Nb		92.90637
41		Molybdenum	Mo		95.95
42		Technetium	Tc		98.0
43		Ruthenium	Ru		101.07
44		Rhodium		Rh		102.9055
45		Palladium	Pd		106.42
46		Silver		Ag		107.8682
47		Cadmium		Cd		112.414
48		Indium		In		114.818
49		Tin		Sn		118.71
50		Antimony	Sb		121.76
51		Tellurium	Te		127.6
52		Iodine		I		126.90447
53		Xenon		Xe		131.293
54		Caesium		Cs		132.90545196
55		Barium		Ba		137.327
56		Lanthanum	La		138.90547
57		Cerium		Ce		140.116
58		Praseodymium	Pr		140.90766
59		Neodymium	Nd		144.242
60		Promethium	Pm		145.0
61		Samarium	Sm		150.36
62		Europium	Eu		151.964
63		Gadolinium	Gd		157.25
64		Terbium		Tb		158.92535
65		Dysprosium	Dy		162.5
66		Holmium		Ho		164.93033
67		Erbium		Er		167.259
68		Thulium		Tm		168.93422
69		Ytterbium	Yb		173.045
70		Lutetium	Lu		174.9668
71		Hafnium		Hf		178.49
72		Tantalum	Ta		180.94788
73		Tungsten	W		183.84
74		Rhenium		Re		186.207
75		Osmium		Os		190.23
76		Iridium		Ir		192.217
77		Platinum	Pt		195.084
78		Gold		Au		196.966569
79		Mercury		Hg		200.592
80		Thallium	Tl		204.38
81		Lead		Pb		207.2
82		Bismuth		Bi		208.9804
83		Polonium	Po		209.0
84		Astatine	At		210.0
85		Radon		Rn		222.0
86		Francium	Fr		223.0
87		Radium		Ra		226.0
88		Actinium	Ac		227.0
89		Thorium		Th		232.0377
90		Protactinium	Pa		231.03588
91		Uranium		U		238.02891
92		Neptunium	Np		237.0
93		Plutonium	Pu		244.0
94		Americium	Am		243.0
95		Curium		Cm		247.0
96		Berkelium	Bk		247.0
97		Californium	Cf		251.0
98		Einsteinium	Es		252.0
99		Fermium		Fm		257.0
100		Mendelevium	Md		258.0
101		Nobelium	No		259.0
102		Lawrencium	Lr		266.0
103		Rutherfordium	Rf		267.0
104		Dubnium		Db		268.0
105		Seaborgium	Sg		269.0
106		Bohrium		Bh		270.0
107		Hassium		Hs		271.0
108		Meitnerium	Mt		278.0
109		Darmstadtium	Ds		281.0
110		Roentgenium	Rg		282.0
111		Copernicium	Cn		285.0
112		Nihonium	Nh		286.0
113		Flerovium	Fl		289.0
114		Moscovium	Mc		290.0
115		Livermorium	Lv		293.0
116		Tennessine	Ts		294.0
117		Oganesson	Og		294.0
'''
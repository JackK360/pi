from decimal import *
from math import pi

N = 100
getcontext().prec = N

x = Decimal(pi)
#numerical approximation 22/7
x0 = Decimal(22) / Decimal(7)
#numerical approximation 355/113
x1 = Decimal(355) / Decimal(113)

print(x)
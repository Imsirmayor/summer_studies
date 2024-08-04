"""
The code below plots the schottky diode graph
"""
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-2, 2, 80)
vd = 15
n = 3
k = 1.380649*10 ** 23 #Boltzmann constant
IS = 3
t= 50 #teprature
q= 10 #elementary charge
vt= k*t/q
nvt=vt * n
ge =vd/nvt #general equation in the bracket
fn = ge - 1 
id = IS * fn 
fig = plt.figure(figsize = (8, 5))
plt.plot(n, id)
plt.show()

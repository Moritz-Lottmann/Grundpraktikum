import numpy as np
from scipy.constants.constants import *
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

l = 0.6
d_oil = 960

li_eta = []
li_r = []
li_d_eta = []
li_d_r = []

def calc(name, diameter, weight, time):
    radius = diameter/1e3/2
    weight = weight/1e6
    d_sphere = weight/(4/3*pi*(radius)**3)

    char_l = 2*radius
    char_v = l/time

    dyn_viscos = 2/9*g*time*radius**2/l*(d_sphere-d_oil)

    kin_viscos = dyn_viscos/d_oil

    Re = char_l*char_v/kin_viscos


    d_t = 0.7
    d_r = 5e-6
    d_l = 2e-3
    d_m = 1e-7
    d_eta = (d_t/time + 5*d_r/radius + d_l/l + d_m/weight) * dyn_viscos
    d_Re = (d_r/radius + d_l/l + d_t/time + d_eta/dyn_viscos) * Re
    # print(name, round(dyn_viscos,3), round(kin_viscos,6), round(Re, 4))
    print(name, round(d_eta, 3))

    li_eta.append(dyn_viscos)
    li_r.append(radius)
    li_d_eta.append((d_eta))
    li_d_r.append(d_r)

calc('A ', 5.99, 882.1, 4.7)
calc('B ', 5.00, 507.1, 6.6)
calc('C ', 3.99, 261.9, 9.8)
calc('D1', 2.98, 110.6, 16.7)
'''calc('D2', 2.98, 110.5, 16.5)
calc('D3', 2.98, 110.5, 16.6)
calc('D4', 2.99, 111.4, 16.4)
calc('D5', 2.98, 110.4, 16.6)
calc('D6', 2.98, 109.9, 16.5)'''
calc('E ', 2.48, 63.7, 23.6)
calc('F ', 1.47, 13.9, 62.6)
calc('G ', 0.99, 3.9, 140.6)



li_eta[3] = 0.939
li_d_eta[3] = 0.024

li_r2 = li_r.copy()
li_r2.pop(5)
li_r_t = np.array(li_r2).reshape((-1,1))
li_eta2 = li_eta.copy()
li_eta2.pop(5)

model = LinearRegression()
model.fit(li_r_t[2:], li_eta2[2:])
r_sqr = model.score(li_r_t[2:], li_eta2[2:])
y_0 = model.intercept_
stg = model.coef_
print(y_0)

plt.errorbar(np.array(li_r)*1000,li_eta, yerr=li_d_eta, linestyle = 'None', marker = 'x')
plt.xlim(left=0)
plt.xlabel("Radius (mm)")
plt.ylabel("Dynamische Viskosität (Pa*s)")
plt.plot([0,max(li_r)*1000], [y_0, max(li_r)*stg+y_0])
plt.show()

import numpy as np
from scipy import stats
from scipy.constants.constants import *
from scipy.stats import linregress as linreg
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

l = 0.6
d_oil = 960

li_v = []
li_r = []

def calc(name, diameter, weight, time):
    radius = diameter/1e3/2
    weight = weight/1e6
    d_sphere = weight/(4/3*pi*(radius)**3)

    char_l = 2*radius
    char_v = l/time

    dyn_viscos = 2/9*g*time*radius**2/l*(d_sphere-d_oil)

    kin_viscos = dyn_viscos/d_oil

    Re = char_l*char_v/kin_viscos

    li_v.append(dyn_viscos)
    li_r.append(radius)

    print(dyn_viscos, kin_viscos, Re)

#calc('A', 5.99, 882.1, 4.7)
#calc('B', 5.00, 507.1, 6.6)
calc('C', 3.99, 261.9, 9.8)
calc('D1', 2.98, 110.6, 16.7)
calc('D2', 2.98, 110.5, 16.5)
calc('D3', 2.98, 110.5, 16.6)
calc('D4', 2.99, 111.4, 16.4)
calc('D5', 2.98, 110.4, 16.6)
calc('D6', 2.98, 109.9, 16.5)
calc('E', 2.48, 63.7, 23.6)
#calc('F', 1.47, 13.9, 62.6)
calc('G', 0.99, 3.9, 140.6)

li_r_t = np.array(li_r).reshape((-1,1))
model = LinearRegression()
model.fit(li_r_t, li_v)
r_sqr = model.score(li_r_t, li_v)
y_0 = model.intercept_

print(y_0)


plt.plot(li_r,li_v, linestyle = 'None', marker = 'o')
plt.show()

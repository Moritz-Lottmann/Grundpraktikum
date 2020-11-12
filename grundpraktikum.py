import numpy as np
from scipy import stats
from scipy.stats import linregress as linreg
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

'''Standardabweichung:'''
def std():
    values = [1,2,3,4,5,6,7,8,100]
    print(np.std(values))
#std()

'''Mittelwert'''
def mwt():
    values = [1,2,3,4,5,6,7,8,9]
    print(np.mean(values))
#mwt()

'''Vertrauenbereich'''
def vtb():
    sigma = 2
    values = [1,2,3,4,5,6,7,8,9]
    n = len(values)
    s = np.std(values)
    out = sigma * s / np.sqrt(n)
    print(out)
#vtb()

li = []

def r(n,l,b,h,m):
    V = l*b*h
    dV = 0.05/l+0.05/b+0.05/h
    r = m/V*1000
    dm = 0.1/m
    dr = dV+dm
    dr2 = dr * r
    #print(n, ': ', round(V,2), ', ', round((dV*100),2), ', ', round(dm*100,2), ', ', round(r,4), ', ', round(dr*100,2), ', ', round(dr2,4))
    #print('')
    li.append((n, round(V,2), round((dV*100),2), round(dm*100,2), round(r,4), round(dr*100,2), round(dr2,4), m))

r(1, 79.7, 30.0, 17.5, 19.2)
r(10, 120.0, 30.7, 17.1, 32.3)
r(17, 80.0, 29.9, 29.7, 31.9)
r(14, 79.8, 29.5, 17.1, 20.3)
r(18, 119.3, 30.6, 17.1, 31.2)
r(9, 40.2, 29.8, 17.2, 8.7)
r(19, 39.8, 30.10, 16.5, 9.3)
r(6, 119.5, 30.0, 17.1, 26.2)
r(12, 119.5, 29.7, 16.9, 26.8)
r(16, 79.7, 28.8, 16.8, 23.0)

# for i in li: print(i)
npli = np.array(li)
v = npli[:, 1]
m = npli[:, -1]
me = npli[:, 3]*m/100
ve = npli[:, 2]*v/100
print(m)
print(me)

plt.errorbar(v,m,yerr=me, xerr=ve, linestyle = 'None', marker = '')
#plt.plot(v,m, linestyle='None', marker='o')
plt.show()

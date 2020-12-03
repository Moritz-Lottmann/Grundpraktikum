import numpy as np
from scipy.constants.constants import g, pi
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression



l = 0.645  # Abstand Auflageschienen
d_l = 0.002
dr_l = d_l/l

k = (5.1 - 0.5)/100/1000  # Umrechnungsfakto
d_k = 2*0.05e-3/100
dr_k = d_k/k

# Berechnung der Fl.trägheitsmomente
I_hohl = pi / 4 * ((8.1e-3/2)**4 - (7.0e-3/2)**4)

I_voll = pi/ 4 * (8.0e-3/2)**4

I_T = 1/12 * ((4.0e-3*(8.0e-3)**3) - (2.6e-3*(5.0e-3)**3))

print(l**3*g/48/I_T/(1.83e-3)*1e-10)

print(I_hohl)
print(I_voll)
print(I_T)
print()

li_m = []
li_d_m = []
li_s = []
li_d_s = []


def calc(I, masse, s_r, s_0):
    if masse in [100, 200, 500]:
        d_m = 0.5e-3
    else:
        d_m = 1e-3

    masse = masse/1000
    s = (s_r - s_0)*k
    E = l**3 * masse * g / 48 / I / s
    d_s = (0.5/s_r + dr_k)*s
    # print(d_s)
    # print(E*1e-10)

    li_m.append(masse)
    li_d_m.append(d_m)
    li_s.append(s)
    li_d_s.append(d_s)
    return E


"""calc(I_hohl, 100, 13, 6.0)
calc(I_hohl, 200, 23.5, 6.0)
calc(I_hohl, 300, 30.5, 6.0)
calc(I_hohl, 400, 37.5, 6.0)
calc(I_hohl, 500, 45, 6.0)"""

print()
calc(I_voll, 100, 9, 1)
calc(I_voll, 200, 18, 1)
calc(I_voll, 300, 27, 1)
calc(I_voll, 400, 36, 1)
calc(I_voll, 500, 45, 1)

"""print()
calc(I_T, 100, 6, 1.5)
calc(I_T, 200, 9.5, 1.5)
calc(I_T, 300, 14, 1.5)
calc(I_T, 400, 17.5, 1.5)
calc(I_T, 500, 22, 1.5)
"""

li_m_t = np.array(li_m).reshape((-1,1))

model = LinearRegression()
model.fit(li_m_t, np.array(li_s), sample_weight=1/np.array(li_d_s))
r_sqr = model.score(li_m_t, np.array(li_s))
y_0 = model.intercept_
stg = model.coef_
print(stg)

plt.errorbar(li_m, np.array(li_s)*1000, xerr=li_d_m, yerr=np.array(li_d_s)*1000, linestyle='None', marker='x')
plt.plot([0,max(li_m)], [y_0*1000, max(li_m)*stg*1000+y_0*1000])
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xlabel("Masse (kg)")
plt.ylabel("Auslenkung (mm)")
plt.title("Auslenkung vs Masse für Vollrohr")
plt.show()


import numpy as np
import sympy as sy
import os
import sys

# https://www.math.stonybrook.edu/~tony/tides/harmonic.html
# w is used in place of ω
# O is used in place of Ω
w1 = 15 # deg/hr
w2 = 0.54901653 # deg/hr
w3 = 0.04106864 # deg/hr
O = 2*(w1 - w2 + w3) # 28.984 deg/hr (from project description)

to_rads = np.pi / 180
to_degs = 180 / np.pi

print(2*(w1 - w2 + w3))

h0, a, b = sy.symbols("h0,a,b")

h = 2.2 
t = 4 + (8/60)
equation_0 = sy.Eq(h0 + a*sy.cos(O*t*to_rads) + b*sy.sin(O*t*to_rads), h)

h = 12.0
t = 9 + (50/60)
equation_1 = sy.Eq(h0 + a*sy.cos(O*t*to_rads) + b*sy.sin(O*t*to_rads), h)

h = 2.4
t = 16 + (22/60)
equation_2 = sy.Eq(h0 + a*sy.cos(O*t*to_rads) + b*sy.sin(O*t*to_rads), h)

results = sy.solve([equation_0, equation_1, equation_2], (h0,a,b), dict=True)[0]
sy.pprint(results)
#print(results[0].keys())

print("t = " + str(float(22+(7/60))))
print("h(t) = " + str(results[h0] + results[a]*np.cos(to_rads*O*(22+(7/60))) + results[b]*np.sin(to_rads*O*(22+(7/60)))))

# results = sy.solve([equation_0, equation_1], (a,b), dict=True)[0]
# #print(results[0].keys())

# print("h(t) = " + str(results[a]*np.cos(to_rads*O*(22+(7/60))) + results[b]*np.sin(to_rads*O*(22+(7/60)))))

# def h(t, h0, a, b):
#     return h0 + a*np.cos(O*t) + b*np.sin(O*t)


import pandas as pd

bristol_data = pd.read_excel(sys.path[0] + "\..\TideData.xlsx", sheet_name = "Bristol")
print(bristol_data.columns)

donaghadee_data = pd.read_excel(sys.path[0] + "\..\TideData.xlsx", sheet_name = "Donaghadee")
print(donaghadee_data.columns)

def lin_eq(h, t):
    return sy.Eq(h0 + a*sy.cos(O*t*to_rads) + b*sy.sin(O*t*to_rads), h)


def solve_system(heights_times):
    eqs = []
    for h_t in heights_times:
        eqs.append(lin_eq(h_t[0], h_t[1]))
    return sy.solve([eqs[0], eqs[1], eqs[2]], (h0,a,b), dict=True)[0]

sp = 0 # start point
inc = 1 # increment

def solve_bristol(sp, inc):
    vals = [[bristol_data["h"][sp], bristol_data['t'][sp]], 
            [bristol_data['h'][sp+inc], bristol_data['t'][sp+inc]], 
            [bristol_data['h'][sp+2*inc], bristol_data['t'][sp+2*inc]]]

    sol = solve_system(vals)
    sy.pprint(sol)
    return sol

def test_results(results, t = 22+(7/60)):
    print("t = " + str(float(t)))
    print("h(t) = " + str(results[h0] + results[a]*np.cos(to_rads*O*(t)) + results[b]*np.sin(to_rads*O*(t))))

def pred_times_highs_lows(a, b):
    print(b/a)
    for n in range(0, 11):
        t = (1/O)*(np.arctan(float(b/a))+np.pi*n)*to_degs # get arg and convert it back into degrees, then use 1/Ω for t
        print(t)
    return t

results = solve_bristol(0,1)
test_results(results)
t = pred_times_highs_lows(results[a], results[b])
test_results(results, t)
# results = solve_bristol(10,1)
# test_results(results)


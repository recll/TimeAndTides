import numpy as np
import sympy as sy

# https://www.math.stonybrook.edu/~tony/tides/harmonic.html
# w is used in place of ω
# O is used in place of Ω
w1 = 15 # deg/hr
w2 = 0.54901653 # deg/hr
w3 = 0.04106864 # deg/hr
O = 2*(w1 - w2 + w3) # 28.984 deg/hr (from project description)

to_rads = np.pi / 180

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

results = sy.solve([equation_0, equation_1], (a,b), dict=True)[0]
#print(results[0].keys())

print("h(t) = " + str(results[a]*np.cos(to_rads*O*(22+(7/60))) + results[b]*np.sin(to_rads*O*(22+(7/60)))))

# def h(t, h0, a, b):
#     return h0 + a*np.cos(O*t) + b*np.sin(O*t)

import pandas as pd
import numpy as np

c_a = 1
m_e = 25 # g

# dati = {
#     #g
#     "m_g": [76.9, 77.3, 62.8],
#     "m_a": [199.9, 201.1, 199.5],
#     #°C
#     "t_g": [0.0, 0.0, 0.0],
#     "t_a": [52.0, 57.0, 54.4],
#     "t_f": [21.6, 24.2, 24.4],
# }
dati = {
    #g
    "m_g": [76.9, 77.3, 62.8, 65.5, 70.7],
    "m_a": [199.9, 201.1, 199.5, 200.7, 203.6],
    #°C
    "t_g": [0.0, 0.0, 0.0, 0.0, 0.0],
    "t_a": [52.0, 57.0, 54.4, 52.2, 58.2],
    "t_f": [21.6, 24.2, 24.4, 24.6, 27.6],
}

m_g = np.array(dati["m_g"])
m_a = np.array(dati["m_a"])
t_g = np.array(dati["t_g"])
t_a = np.array(dati["t_a"])
t_f = np.array(dati["t_f"])


d_m_e = 5
d_m = 0.1
d_t = 0.2

M_1 = m_a + m_e
M_2 = m_g
DT_1 = t_a - t_f
DT_2 = t_f - t_g

d_M_1 = np.sqrt(d_m_e**2 + d_m**2)
d_M_2 = d_m
d_T_1 = d_t*np.sqrt(2)
d_T_2 = d_t*np.sqrt(2)

ni_M_1 = d_M_1/M_1
ni_M_2 = d_M_2/M_2
ni_T_1 = d_T_1/DT_1
ni_T_2 = d_T_2/DT_2


cl = (c_a/M_2) * (M_1*DT_1 - M_2*DT_2) * (DT_1 / DT_2)
d_cl = cl*np.sqrt(ni_M_1**2 + ni_M_2**2 + ni_T_1**2 + ni_T_2**2)

print(pd.DataFrame(dati).to_latex())

print(pd.DataFrame({
    "c": cl
}).to_latex())

print(pd.DataFrame({
    "c": cl,
    "dc": d_cl,
}))
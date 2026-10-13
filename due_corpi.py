import pandas as pd
import numpy as np

c_a = 1
m_e = 25 # g

# DATI alluminio
# dati = {
#     # g
#     "m_1": [80.1, 80.1, 80.1, 80.1, 80.1],
#     "m_a": [200.0, 201.0, 206.3, 198.9, 200.7],
#     # °C
#     "t_1": [64.6, 64.2, 68.0, 59.4, 57.8],
#     "t_a": [19.2, 24.6, 23.2, 28.6, 17.8], 
#     "t_f": [22.0, 27.4, 26.4, 30.6, 20.6],
# }

# DATI ottone
# dati = {
#     # g
#     "m_1": [194.5, 194.5],
#     "m_a": [200.2, 201.0],
#     # °C
#     "t_1": [55.6, 59.2],
#     "t_a": [16.2, 24.0], 
#     "t_f": [19.4, 26.8],
# }

# DATI okite
# dati = {
#     # g
#     "m_1": [115.6, 115.6],
#     "m_a": [201.4, 200.8],
#     # °C
#     "t_1": [56.2, 57.4],
#     "t_a": [16.4, 24.0], 
#     "t_f": [20.0, 27.0],
# }

# DATI granito
dati = {
    # g
    "m_1": [19.2, 19.2],
    "m_a": [200.3, 206.1],
    # °C
    "t_1": [58.0, 66.2],
    "t_a": [16.2, 20.6], 
    "t_f": [17.4, 22.0],
}


m_1 = np.array(dati["m_1"])
m_a = np.array(dati["m_a"])
t_1 = np.array(dati["t_1"])
t_a = np.array(dati["t_a"])
t_f = np.array(dati["t_f"])


d_m_e = 5
d_m = 0.1
d_t = 0.2

M_1 = m_a + m_e
M_2 = m_1
DT_1 = t_f - t_a
DT_2 = t_1 - t_f

d_M_1 = np.sqrt(d_m_e**2 + d_m**2)
d_M_2 = d_m
d_T_1 = d_t*np.sqrt(2)
d_T_2 = d_t*np.sqrt(2)

ni_M_1 = d_M_1/M_1
ni_M_2 = d_M_2/M_2
ni_T_1 = d_T_1/DT_1
ni_T_2 = d_T_2/DT_2


c_1 = c_a * (M_1 / M_2) * (DT_1 / DT_2)
d_c_1 = c_1*np.sqrt(ni_M_1**2 + ni_M_2**2 + ni_T_1**2 + ni_T_2**2)

print(pd.DataFrame(dati).to_latex())

print(pd.DataFrame({
    "c": c_1
}).to_latex())

print(pd.DataFrame({
    "c": c_1,
    "dc": d_c_1,
}))


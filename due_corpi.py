import pandas as pd
import numpy as np

c_a = 1
m_a = 0
m_e = 25 # g

# DATI
m_1 = np.array([3,2,1])
t_1 = np.array([[9,6,8], [2,1,2], [4,6,4]])
t_a = np.array([[6,7,8], [1,1,3], [5,6,6]])
t_f = np.array([[3,4,3], [1,1,2], [10,10,12]])


d_m_e = 5
d_m = 0.1
d_t = 0.1

M_1 = m_a + m_e
M_2 = m_1
DT_1 = t_f.mean() - t_a.mean()
DT_2 = t_1.mean() - t_f.mean()

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


print(c_1, d_c_1)
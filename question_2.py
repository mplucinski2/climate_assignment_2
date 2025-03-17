import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

alpha = 10.0 
total_nox_vals = np.arange(0, 51, 1) 

results = []  
for total_nox in total_nox_vals:
    NO0 = total_nox
    NO20 = 0.0
    O30 = 0.0
    O3_ss1 = -0.5*(NO0 - O30 + alpha) + 0.5*math.sqrt((NO0 - O30 + alpha)**2 + 4*alpha*(NO20 + O30))
    NO0 = 0.0
    NO20 = total_nox
    O30 = 0.0
    O3_ss2 = -0.5*(NO0 - O30 + alpha) + 0.5*math.sqrt((NO0 - O30 + alpha)**2 + 4*alpha*(NO20 + O30))
    NO0 = total_nox / 2.0
    NO20 = total_nox / 2.0
    O30 = 0.0
    O3_ss3 = -0.5*(NO0 - O30 + alpha) + 0.5*math.sqrt((NO0 - O30 + alpha)**2 + 4*alpha*(NO20 + O30))
    results.append([total_nox, O3_ss1, O3_ss2, O3_ss3])

df_ss = pd.DataFrame(results, columns=["Total_NOx (nmol/mol)",
                                       "O3_ss_NO_only (nmol/mol)",
                                       "O3_ss_NO2_only (nmol/mol)",
                                       "O3_ss_equal_NO_NO2 (nmol/mol)"])
df_ss.to_csv("steady_state_scenarios.csv", index=False)

plt.figure(figsize=(6,5))
plt.plot(df_ss["Total_NOx (nmol/mol)"], df_ss["O3_ss_NO_only (nmol/mol)"], label="Initial NO only")
plt.plot(df_ss["Total_NOx (nmol/mol)"], df_ss["O3_ss_NO2_only (nmol/mol)"], label="Initial $\\mathregular{NO_2}$ only")
plt.plot(df_ss["Total_NOx (nmol/mol)"], df_ss["O3_ss_equal_NO_NO2 (nmol/mol)"], label="Equal NO & $\\mathregular{NO_2}$")
plt.xlabel("Initial total $\\mathregular{NO_x}$ ($\\mathregular{[\\frac{nmol}{mol}]}$")
plt.ylabel("Steady-state $\\mathregular{O_3}$ $\\mathregular{[\\frac{nmol}{mol}]}$")
plt.legend()
plt.grid(True)
plt.savefig("question_2.svg")
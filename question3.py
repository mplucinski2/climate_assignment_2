import numpy as np
import matplotlib.pyplot as plt


# Given data
T = 298  # Temperature in K
c_air = 2.69e19  # Air density in molecules/cm³
CO_mixing_ratio = 4500e-9  # CO mixing ratio in mol/mol
NO2_NO_ratio = 7  # NO2/NO ratio
PHOx_mixing_ratio = 1.2e-3 * 1e-9  # PHOx in mol/mol/s

# Convert to molecules/cm³
CO_concentration = CO_mixing_ratio * c_air  # [CO] in molecules/cm³
PHOx = PHOx_mixing_ratio * c_air  # PHOx in molecules/cm³/s
print(PHOx)
# PHOx = PHOx_mixing_ratio

# Reaction rate constants (from Table 3, assumed values)
k_HO2_HO2 = 6.1e-12  # cm³/molecule/s
k_OH_NO2 = 9.0e-12  # cm³/molecule/s
k_CO_OH = 1.57e-13+(c_air*3.54e-33)  # cm³/molecule/s
k_HO2_NO = 3.3e-12*np.exp(270/T)  # cm³/molecule/s

# Define NO concentration range
NO_range = np.linspace(0, 6e10, 100)  # [NO] in molecules/cm³
NO2_concentration = NO2_NO_ratio * NO_range  # [NO2] from ratio

# Compute quadratic coefficients
a = 2 * k_HO2_HO2 * (1 + (k_OH_NO2 * NO2_concentration) / (k_CO_OH * CO_concentration))
b = (k_HO2_NO * k_OH_NO2 * NO2_concentration * NO_range) / (k_CO_OH * CO_concentration)
c = -PHOx

# Solve quadratic equation for [HO2]
HO2_concentration = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Compute O3 production rate
PO3 = k_HO2_NO * HO2_concentration * NO_range
# NO_range[0] = 1e5
# Plot [HO2] vs [NO]
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(NO_range, HO2_concentration, label='[HO2]', color='b')
#make x axis logarithmic
plt.xscale('log')
plt.xlabel('[NO] (molecules/cm³)')
plt.ylabel('[HO2] (molecules/cm³)')
plt.title('HO2 Concentration vs. NO')
plt.grid(True)

# Plot PO3 vs [NO]
plt.subplot(1, 2, 2)
plt.plot(NO_range, PO3, label='PO3', color='r')
plt.xscale('log')
plt.xlabel('[NO] (molecules/cm³)')
plt.ylabel('PO3 (molecules/cm³/s)')
plt.title('Ozone Production Rate vs. NO')
plt.grid(True)

plt.tight_layout()
plt.show()

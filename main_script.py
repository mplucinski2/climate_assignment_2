import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ozone_df = pd.read_csv("yearmean_RD1_2019_zm.csv")

print(ozone_df.columns)
print(ozone_df.head(5))

R = 8.314 
N_A = 6.022e23  
ozone_df['O3_concentration_molec_cm3'] = ozone_df.apply(lambda row: row['O3'] * (row['plev'] / (R * row['tm1'])) * (N_A / 1e6), axis=1)
ozone_df.to_csv("ozone_with_concentration.csv", index=False)
ozone_df = ozone_df.drop_duplicates(subset=['lat', 'plev'])

mixing_ratio_pivot = ozone_df.pivot(index='lat', columns='plev', values='O3')
conc_pivot = ozone_df.pivot(index='lat', columns='plev', values='O3_concentration_molec_cm3')

lats = mixing_ratio_pivot.index.values
plevs = mixing_ratio_pivot.columns.values

mixing_ratio_grid = mixing_ratio_pivot.values
conc_grid = conc_pivot.values

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
params = {'mathtext.default': 'regular' }          


cp1 = axes[0].contourf(lats, plevs, mixing_ratio_grid.T * 1e6, levels=20, cmap='viridis')
axes[0].invert_yaxis()  
axes[0].set_ylabel("pressure [hPa]")
axes[0].set_yscale('log')
axes[0].set_xlabel("latitude [deg]")
fig.colorbar(cp1, ax=axes[0], label="$\mathregular{O_3}$ [ppm]")

cp2 = axes[1].contourf(lats, plevs, conc_grid.T, levels=20, cmap='plasma')
axes[1].invert_yaxis()
axes[1].set_yscale('log')
axes[1].set_xlabel("latitude [deg]")
fig.colorbar(cp2, ax=axes[1], label="$\mathregular{O_3}$ [molec/cm³]")

plt.tight_layout()
plt.savefig("ozone_lat_pressure_plots.svg")
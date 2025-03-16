"""
Module for analyzing aircraft emissions data.
"""

import csv
import numpy as np
from os import path
import matplotlib.pyplot as plt

#define path using os.path.join
file_paths = [path.join('O3_NO_NO2_measurements', 'airbase_DEBY109_NO.csv'),
              path.join('O3_NO_NO2_measurements', 'airbase_DEBY109_NO2.csv'),
              path.join('O3_NO_NO2_measurements', 'airbase_DEBY109_O3.csv')]

Data_DEBY = []
#import csv files
for i, file_path in enumerate(file_paths):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        data = np.array(data)
        data = data[1:, :] # omit the header
        column_data = data[:, 1] # keep second column
        column_data = column_data[:-1] # remove last row
        column_data = np.array([float(x) if x else np.nan for x in column_data]) # convert to float
        Data_DEBY.append(column_data)
Data_DEBY = np.array(Data_DEBY)



file_paths = [path.join('O3_NO_NO2_measurements', 'airbase_NL00131_NO.csv'),
              path.join('O3_NO_NO2_measurements', 'airbase_NL00131_NO2.csv'),
              path.join('O3_NO_NO2_measurements', 'airbase_NL00131_O3.csv')]
Data_NL1 = []
for i, file_path in enumerate(file_paths):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        data = np.array(data)
        data = data[1:, :] # omit the header
        column_data = data[:, 1] # keep second column
        column_data = column_data[:-1] # remove last row
        column_data = np.array([float(x) if x else np.nan for x in column_data]) # convert to float
        Data_NL1.append(column_data)

Data_NL1 = np.array(Data_NL1)


file_paths = [path.join('O3_NO_NO2_measurements', 'airbase_NL00418_NO.csv'),
                path.join('O3_NO_NO2_measurements', 'airbase_NL00418_NO2.csv'),
                path.join('O3_NO_NO2_measurements', 'airbase_NL00418_O3.csv')]
Data_NL2 = []

for i, file_path in enumerate(file_paths):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        data = np.array(data)
        data = data[1:, :] # omit the header
        column_data = data[:, 1] # keep second column
        column_data = column_data[:-1] # remove last row
        column_data = np.array([float(x) if x else np.nan for x in column_data]) # convert to float
        Data_NL2.append(column_data)
Data_NL2 = np.array(Data_NL2)

# Create a figure with 3 subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 18), sharex=True, sharey=True)

# Scatter plot for DEBY109
axs[0].scatter(Data_DEBY[0] + Data_DEBY[1], Data_DEBY[2], label='DEBY109')
axs[0].set_xscale('log')
axs[0].set_xlim(left=1e-2)  # Increase the range of x on the lower side
axs[0].set_ylabel('O3 (molecules/cm³)')
axs[0].set_title('Ozone vs. NOx for DEBY109')
axs[0].legend()
axs[0].grid(True)

# Scatter plot for NL00131
axs[1].scatter(Data_NL1[0] + Data_NL1[1], Data_NL1[2], label='NL00131')
axs[1].set_xscale('log')
axs[1].set_xlim(left=1e-2)  # Increase the range of x on the lower side
axs[1].set_ylabel('O3 (molecules/cm³)')
axs[1].set_title('Ozone vs. NOx for NL00131')
axs[1].legend()
axs[1].grid(True)

# Scatter plot for NL00418
axs[2].scatter(Data_NL2[0] + Data_NL2[1], Data_NL2[2], label='NL00418')
axs[2].set_xscale('log')
axs[2].set_xlim(left=1e-2)  # Increase the range of x on the lower side
axs[2].set_xlabel('NOx (molecules/cm³)')
axs[2].set_ylabel('O3 (molecules/cm³)')
axs[2].set_title('Ozone vs. NOx for NL00418')
axs[2].legend()
axs[2].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()


import pandas as pd
import math

alpha = 10.0 
stations = ["NL00131", "DEBY109", "NL00418"]
pollutants = ["NO", "NO2", "O3"]
mean_vals = {}  

for st in stations:
    mean_vals[st] = {}
    for pol in pollutants:
        df_pol = pd.read_csv(f"O3_NO_NO2_measurements/airbase_{st}_{pol}.csv")
        mean_conc = df_pol.iloc[:, 1].mean(skipna=True)
        mean_vals[st][pol] = mean_conc

conv_factors = {"NO": 1.3, "NO2": 1.9, "O3": 2.0}
for st in stations:
    NO_ppb = mean_vals[st]["NO"] / conv_factors["NO"]
    NO2_ppb = mean_vals[st]["NO2"] / conv_factors["NO2"]
    O3_ppb = mean_vals[st]["O3"] / conv_factors["O3"]
    NO0 = NO_ppb
    NO20 = NO2_ppb
    O30 = 0.0
    O3_ss = -0.5*(NO0 - O30 + alpha) + 0.5*math.sqrt((NO0 - O30 + alpha)**2 + 4*alpha*(NO20 + O30))
    mean_vals[st]["NO_ppb"] = NO_ppb
    mean_vals[st]["NO2_ppb"] = NO2_ppb
    mean_vals[st]["O3_ppb"] = O3_ppb
    mean_vals[st]["O3_ss_ppb"] = O3_ss

summary_df = pd.DataFrame.from_dict(mean_vals, orient='index')
summary_df.to_csv("station_annual_means.csv", index=True)
print(summary_df[["NO_ppb","NO2_ppb","O3_ppb","O3_ss_ppb"]])

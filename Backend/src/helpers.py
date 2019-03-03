import pandas as pd

df = pd.read_excel('./data/car_efficiency.xlsx')
df.sort_values(by=['Mfr Name'])


def calc_emission_driver(mdf, division, carline, g_to_m, index, eng, cyl, tran, d):
    vehicle = df.loc[(df['Mfr Name'] == mdf) & (df['Division'] == division) & 
    (df['Carline'] == carline) & (df['Verify Mfr Cd'] == g_to_m) & 
    (df['Index (Model Type Index)'] == index) & (df['Eng Displ'] == eng) & (df['# Cyl'] == cyl) & 
    (df['Transmission'] == tran)]
    return vehicle['Comb Unadj FE - Conventional Fuel'].iloc[0] / d * 9.072 / 1000


def calc_emission(persona):
    if persona == "driver":
        return 120
    if persona == "Farmer/Producer":
        return 80
    if persona == "Storage companies":
        return 50
    if persona == "Food processor":
        return 50
    if persona == "Trader/Distributor":
        return 60







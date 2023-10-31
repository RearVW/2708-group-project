import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import geopandas

pd.set_option('display.max_columns', 4)
df_gas = pd.read_csv('data\df_gas.csv')
#df_gas = df_gas.loc[df_gas['tg_consumption_gwh'] > 5]
df_gas_pb = df_gas.loc[df_gas['housing_type'] == 'Public Housing']
df_gas_1_2 = df_gas.loc[df_gas['dwelling_type'] == '1-Room / 2-Room']

print(df_gas_1_2)

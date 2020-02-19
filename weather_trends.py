import numpy as np
import pandas as pd

berlin_data = pd.read_csv("Data/berlin_data.csv")
global_data = pd.read_csv("Data/global_data.csv")

if(global_data.duplicated('year').sum() == 0):
    print("Global DataSet:\nData available for {} year from {} to {}".format(global_data.year.count(),global_data.year.min(),global_data.year.max()))
else:
    print("There are duplicates")

if (global_data.isna().sum().sum()) == 0:
    print("No missing value in Global DataSet\n")
else:
    global_data_nan = global_data[global_data.isna().any(axis=1)]
    print("Missing values from Global Data", global_data_nan)

if(berlin_data.duplicated('year').sum() == 0):
    print("Berlin DataSet:\nData available for {} year from {} to {}".format(berlin_data.year.count(),berlin_data.year.min(),berlin_data.year.max()))
else:
    print("There are duplicates")

if (berlin_data.isna().sum().sum()) == 0:
    print("No missing value in Berlin Data")
else:
    berlin_data_nan = berlin_data[berlin_data.isna().any(axis=1)]
    print("Missing values from Berlin DataSet:\n\n", berlin_data_nan)

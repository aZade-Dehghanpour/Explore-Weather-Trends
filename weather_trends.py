import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

start_year = max([berlin_data.year.min(),global_data.year.min()])
end_year = min([berlin_data.year.max(),global_data.year.max()])

berlin_data_new = berlin_data[berlin_data.year.between(start_year,end_year)]
berlin_data_new.reset_index(drop=True,inplace=True)
global_data_new = global_data[global_data.year.between(start_year,end_year)]
global_data_new.reset_index(drop=True,inplace=True)
berlin_data_new['mv_avg']=berlin_data_new['avg_temp'].rolling(window=30).mean()
global_data_new['mv_avg']=global_data_new['avg_temp'].rolling(window=30).mean()

year = berlin_data_new.year

plt.figure(figsize = (15,10))
plt.grid(True)
plt.plot(year, berlin_data_new['mv_avg'],label = "Brl MA 30 y")
plt.plot(year, global_data_new['mv_avg'],label = "GL MA 30 y")
plt.xlabel('Years')
plt.ylabel('Average Temprature')
plt.legend(loc = 2)
berlin_plot_min=berlin_data_new['mv_avg'].min()
year_point=int(berlin_data_new[berlin_data_new['mv_avg']==berlin_plot_min].year.values)
plt.text(year_point,berlin_plot_min,"Year: {}\n avg_temp:{}".format(year_point,berlin_plot_min))
global_plot_min=global_data_new['mv_avg'].min()
gl_year_point=int(global_data_new[global_data_new['mv_avg']==global_plot_min].year.values)
plt.text(gl_year_point,global_plot_min,"Year: {}\n avg_temp:{}".format(gl_year_point,global_plot_min))
#berlin
plt.text(berlin_data_new.iloc[29].year,berlin_data_new.iloc[29].mv_avg,"Year: {}\n avg_temp:{}".format(berlin_data_new.iloc[29].year,berlin_data_new.iloc[29].mv_avg))
plt.text(berlin_data_new.iloc[-1].year,berlin_data_new.iloc[-1].mv_avg,"Year: {}\n avg_temp:{}".format(berlin_data_new.iloc[-1].year,berlin_data_new.iloc[-1].mv_avg))

plt.text(global_data_new.iloc[29].year,global_data_new.iloc[29].mv_avg,"Year: {}\n avg_temp:{}".format(global_data_new.iloc[29].year,global_data_new.iloc[29].mv_avg))
plt.text(global_data_new.iloc[-1].year,global_data_new.iloc[-1].mv_avg,"Year: {}\n avg_temp:{}".format(global_data_new.iloc[-1].year,global_data_new.iloc[-1].mv_avg))


plt.show()

import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

def get_weather_data(date,time):
    df_weather = pd.read_csv(
        'C:/Users/Ve/Documents/GitHub/eismoinfo-weather/LOGS/'+"EIW_"+ date.replace("-", "") +'.csv', index_col=None, header=0)
    df_stations = pd.read_csv(
        'C:/Users/Ve/Documents/GitHub/eismoinfo-weather/stations.csv', index_col=None, header=0)
    df_weather.sort_values(by=['timestamp'], ascending=False)
    df_weather = df_weather[df_weather['timestamp']< date +" "+ time]
    df_stations = df_stations[['station_UID', 'station_name', 'lat_LKS94', 'long_LKS94']]
    df = df_weather.merge(df_stations, on='station_UID') #join table of weather data and static table with station locations
    df.drop_duplicates(subset=['station_UID'], inplace=True)
    return df


print("############################## PROCESS ##############################")

date = '2021-10-16'
time = '07:00'

df = get_weather_data(date,time)


plt.style.use('dark_background')
plt.figure(figsize=(10,36))

subplot_count = 3

plt.subplot(subplot_count,1,1)
plot_as_surface(df,'air_temp_C','coolwarm')

plt.subplot(subplot_count,1,2)
plot_as_surface(df,'wind_spd_avg_ms','plasma')

plt.subplot(subplot_count,1,3)
plot_as_surface(df,'wind_dir','plasma')

'''
plt.subplot(subplot_count, 1, 4)
plot_as_surface(df,'Precipitation amount [mm/h]','prcp_amount_mm','Blues')

plt.subplot(subplot_count, 1, 5)
plot_as_surface(df,'Visibility [m]','visibility_m','Blues')
'''

plt.tight_layout()
plt.savefig('./reports/Report.png', dpi=600, orientation='portrait')
#plt.show()
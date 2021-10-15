import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation, LinearTriInterpolator

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

date = '2021-10-14'
time = '15:00'

df = get_weather_data(date,time)

field_to_plot = 'prcp_amount_mm'
df.dropna(subset = [field_to_plot], inplace=True) #drop null values
df.index = range(0,len(df))


totalPointsArray = np.zeros([
    len(df)+1,
    3])

for index, row in df.iterrows():
    print(row["lat_LKS94"])
    if (pd.isnull(row[field_to_plot])):
        print("NULL")
    else:
        pointArray = np.array([row["long_LKS94"],
                               row["lat_LKS94"],
                               row[field_to_plot]
                               ])

    totalPointsArray[index] = pointArray

totalPointsArray = np.delete(totalPointsArray, (-1), axis=0)
np.set_printoptions(suppress=True)
print(totalPointsArray)


#triangulation function
triFn = Triangulation(totalPointsArray[:,0],totalPointsArray[:,1])
#linear triangule interpolator funtion
linTriFn = LinearTriInterpolator(triFn,totalPointsArray[:,2])

#define raster resolution in (m)
rasterRes = 5000

xCoords = np.arange(totalPointsArray[:,0].min(), totalPointsArray[:,0].max()+rasterRes, rasterRes)
yCoords = np.arange(totalPointsArray[:,1].min(), totalPointsArray[:,1].max()+rasterRes, rasterRes)
zCoords = np.zeros([yCoords.shape[0],xCoords.shape[0]])

#loop among each cell in the raster extension
for indexX, x in np.ndenumerate(xCoords):
    for indexY, y in np.ndenumerate(yCoords):
        tempZ = linTriFn(x,y)
        #filtering masked values
        if tempZ == tempZ:
            zCoords[indexY,indexX]=tempZ
        else:
            zCoords[indexY,indexX]=np.nan

zCoords = np.rot90(zCoords, 1)

#preliminary representation of the interpolated values
plt.imshow(zCoords, interpolation='none')
plt.show()

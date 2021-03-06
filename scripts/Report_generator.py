import pandas as pd
import numpy as np
import seaborn as sns
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from datetime import datetime


def get_weather_data(date,time):
    print("---------------- SCAN WEATHER LOGS ----------------")
    df_weather = pd.read_csv(
        'C:/Users/Ve/Documents/GitHub/eismoinfo-weather/LOGS/'+"EIW_"+ date.replace("-", "") +'.csv', index_col=None, header=0)
    df_stations = pd.read_csv(
        'C:/Users/Ve/Documents/GitHub/eismoinfo-weather/stations.csv', index_col=None, header=0)
    df_weather.sort_values(by=['timestamp'], ascending=False)
    df_weather = df_weather[df_weather['timestamp']< date +" "+ time]
    df_stations = df_stations[['station_UID', 'station_name', 'lat_LKS94', 'long_LKS94']]
    df = df_weather.merge(df_stations, on='station_UID') #join table of weather data and static table with station locations
    df.drop_duplicates(subset=['station_UID'], inplace=True)
    print("---------------- RETURN DATAFRAME ----------------")
    print(df)
    print("\n")
    return df




def add_station_layer(df):
    print("---------------- ADD STATTION POINTS ----------------")
    y = df["long_LKS94"]
    x = df["lat_LKS94"]
    plt.scatter(x, y, facecolors='grey', edgecolors='white', s=20)
    plt.autoscale(False)
    plt.xticks([])
    plt.yticks([])
    print("\n")




LTU_x = [554670, 556622, 555891, 559912, 560230, 565447, 567792, 572439, 576577, 581711, 587225, 588292, 588943, 593511, 593780, 595408, 597291, 599583, 602623, 603950, 605690, 605038, 613367, 615871, 616039, 623215, 624873, 627768, 632664, 636683, 639637, 642351, 645250, 647554, 649287, 654417, 659197, 665412, 665477, 659430, 661687, 660788, 661999, 660632, 661815, 656864, 656738, 654740, 662706, 665466, 666638, 667055, 669005, 672620, 677180, 679790, 680101, 673670, 673690, 670282, 672357, 670589, 670062, 661914, 660372, 656945, 654511, 652785, 650076, 646806, 644199, 642247, 645032, 642884, 643280, 641301, 635409, 635074, 632926, 632106, 627059, 622301, 619073, 618863, 614426, 613962, 612025, 611573, 613952, 608873, 606228, 603883, 605544, 605955, 604229, 603268, 603538, 601518, 601166, 599624, 601002, 609576, 611349, 610617, 613575, 616335, 614127, 615992, 616607, 611238, 610087, 607121, 606027, 600185, 598967, 601937, 600891, 603665, 601113, 601801, 598995, 598499, 597414, 597617, 595448, 593350, 588185, 584110, 582721, 581562, 580416, 579450, 577987, 569965, 564892, 562508, 556564, 553141, 554324, 550582, 550787, 553647, 553873, 556988, 554503, 553474, 550438, 549514, 548479, 544924, 546253, 544805, 543267, 541025, 533926, 530997, 518293, 516436, 513802, 513227, 509333, 507512, 506769, 501997, 497834,
         497464, 494293, 492589, 489584, 486679, 480933, 473603, 472521, 469608, 466486, 465953, 468873, 469143, 466415, 464680, 462428, 459659, 456829, 450087, 448072, 444943, 444615, 440908, 437676, 439082, 434613, 435705, 434003, 425653, 421494, 418042, 415777, 414607, 416790, 414903, 419215, 419805, 417685, 419379, 418943, 421081, 423208, 423616, 425604, 428437, 426683, 427381, 425518, 426007, 424351, 422640, 422002, 420174, 420962, 419400, 415428, 414186, 414440, 413177, 410243, 409898, 402546, 390892, 382324, 379720, 376955, 374179, 374334, 371793, 370044, 367112, 362683, 360661, 354643, 350421, 345218, 340973, 333899, 326485, 315563, 306496, 312955, 316834, 317755, 317401, 316391, 315546, 317173, 317247, 323243, 325863, 328335, 328008, 331073, 334370, 342107, 345223, 347365, 349130, 351750, 359252, 366299, 368568, 374826, 376073, 377845, 379604, 384669, 386829, 389542, 391394, 395799, 398037, 403098, 414537, 418411, 421545, 428241, 432034, 433844, 434614, 436390, 438416, 439822, 440935, 442500, 443883, 449550, 448742, 455691, 457164, 462196, 465319, 471857, 477139, 485470, 486439, 485578, 486482, 487858, 501171, 501400, 503048, 502849, 506062, 507538, 510957, 512455, 517965, 517685, 521011, 522160, 524284, 528151, 535877, 535677, 538553, 538836, 542622, 543330, 547877, 549782, 550877, 553163, 552501, 554670]
LTU_y = [6257793, 6256778, 6253632, 6248401, 6242278, 6237410, 6228569, 6227297, 6229403, 6224230, 6225822, 6224370, 6225431, 6224432, 6226057, 6226798, 6223995, 6223439, 6223568, 6225223, 6221923, 6218242, 6214909, 6211387, 6208855, 6207029, 6204991, 6204117, 6195935, 6194840, 6191560, 6183796, 6181118, 6181146, 6177530, 6177368, 6174253, 6174911, 6162093, 6155664, 6150566, 6149110, 6147755, 6147863, 6142259, 6139989, 6138498, 6137448, 6134541, 6134679, 6136429, 6134999, 6136969, 6135198, 6135313, 6133824, 6131453, 6126700, 6123409, 6121245, 6118484, 6118248, 6116623, 6114899, 6116815, 6113086, 6114337, 6113533, 6115301, 6112366, 6111853, 6110035, 6107005, 6105483, 6102804, 6097954, 6096787, 6094925, 6094657, 6091458, 6093126, 6090042, 6089533, 6086072, 6081562, 6077784, 6076820, 6062082, 6050349, 6045718, 6038546, 6037188, 6036591, 6033071, 6030021, 6030559, 6027662, 6026555, 6023937, 6023454, 6020884, 6021548, 6019110, 6017270, 6016521, 6012676, 6010829, 6008387, 6003392, 6004859, 6001688, 6000166, 6001892, 6003170, 6006517, 6008016, 6011167, 6011717, 6015402, 6016433, 6017048, 6020039, 6020229, 6019165, 6017961, 6018564, 6014942, 6014613, 6016102, 6013384, 6014730, 6014161, 6009083, 6000119, 6001215, 6004290, 6001422, 6001146, 5999783, 5998108, 5996555, 5992694, 5989866, 5988559, 5988065, 5984602, 5983883, 5984905, 5981187, 5980720, 5986047, 5986921, 5985539, 5986069, 5981106, 5976987, 5976987, 5979503, 5979149, 5981400, 5979591, 5980053, 5978104, 5976987, 5976987,
         5979662, 5981349, 5978492, 5979820, 5976987, 5978020, 5976987, 5978426, 5978343, 5982024, 5984622, 5988282, 5992142, 6001893, 6004388, 6004628, 6010373, 6012934, 6014025, 6017132, 6018103, 6020036, 6018313, 6020305, 6023067, 6025460, 6027770, 6028549, 6030995, 6025824, 6034745, 6035977, 6044839, 6048233, 6050479, 6055649, 6058058, 6061819, 6064073, 6066481, 6069008, 6068620, 6070670, 6070663, 6075881, 6078687, 6080247, 6081512, 6085189, 6086858, 6085936, 6088321, 6087639, 6089522, 6090001, 6095395, 6094811, 6092885, 6093510, 6099782, 6104718, 6102039, 6104579, 6103760, 6100602, 6100435, 6103204, 6107191, 6107424, 6106069, 6106901, 6108896, 6111467, 6113269, 6118606, 6120791, 6119545, 6131884, 6126664, 6128387, 6131497, 6144923, 6159554, 6175532, 6180270, 6180810, 6202095, 6208226, 6218908, 6220559, 6219434, 6224438, 6228847, 6230083, 6234851, 6237915, 6242958, 6242708, 6245198, 6246032, 6244571, 6250794, 6249591, 6251233, 6255170, 6256419, 6255454, 6256995, 6255545, 6255957, 6253251, 6254242, 6252384, 6253999, 6250770, 6247244, 6249579, 6248553, 6249519, 6251025, 6253974, 6253873, 6253012, 6244612, 6243358, 6243818, 6241604, 6245182, 6248473, 6248952, 6250179, 6249672, 6246625, 6244385, 6247452, 6248906, 6248276, 6243376, 6243024, 6245434, 6244030, 6241911, 6240646, 6238455, 6238191, 6235035, 6235264, 6237069, 6239153, 6240827, 6240338, 6237694, 6238385, 6236151, 6239563, 6243445, 6245999, 6249302, 6249515, 6252499, 6252067, 6254582, 6253341, 6253934, 6256184, 6257793]




def add_LTUBorder_layer(LTU_x, LTU_y):
    print("---------------- ADD LTU AREA ----------------")
    external_polygon_y = [6263556, 6263556, 5969088, 5969088, 6263556]
    external_polygon_x = [686663, 297644, 297644, 686663, 686663]

    # if you don't specify a color, you will see a seam
    plt.fill(external_polygon_x+LTU_x,
             external_polygon_y+LTU_y,
             color='black')

    plt.gca().set_aspect('equal',adjustable='box') #prevents map aspect ratio distortion
    plt.xlim(min(external_polygon_x), max(external_polygon_x))
    plt.ylim(min(external_polygon_y), max(external_polygon_y))

    plt.plot(LTU_x, LTU_y, color="grey", alpha=0.85, linewidth=2.5)
    print("\n")




def interpolate_XYZ(x, y, z, resolution=50, contour_method='cubic'):
    resolution = str(resolution)+'j'
    X, Y = np.mgrid[min(x):max(x):complex(resolution),
                    min(y):max(y):complex(resolution)]
    points = [[a, b] for a, b in zip(x, y)]
    Z = griddata(points, z, (X, Y),
                 method=contour_method,
                 fill_value=np.average(z))
    return X, Y, Z




def add_name(name):
    print("-------- ADD NAME --------")
    date_time_min =  datetime.strptime(df['timestamp'].min(), '%Y-%m-%d %H:%M')
    date_time_max =  datetime.strptime(df['timestamp'].max(), '%Y-%m-%d %H:%M')

    title = "   |   " + name + "   |   " + "date %s-%s-%s    |   time %s:%s - %s:%s" % (date_time_min.year,
                                                                                           date_time_min.month,
                                                                                           date_time_min.day,
                                                                                           date_time_min.hour,
                                                                                           date_time_min.minute,
                                                                                           date_time_max.hour,
                                                                                           date_time_max.minute) + "   |   "
    plt.title(title)




def add_statistics(df,field_to_plot):
    print("-------- ADD STATS AS TEXT --------")
    plot_val_min = df[field_to_plot].min()
    plot_val_max = df[field_to_plot].max()
    plot_val_range = round(plot_val_max-plot_val_min, 1)
    statistics = "min: " + str(plot_val_min) + "\n" + "max: " + str(plot_val_max) + "\n" + "range: " + str(plot_val_range)

    font2 = {'family': 'Arial',
             'color': 'grey',
             'weight': 'normal',
             'size': 16,
             }
    
    plt.text(319117, 5983941, statistics, fontdict=font2)





def plot_as_surface(df,field_to_plot,colormap):
    print("---------------- PLOT SURFACE OF ----------------")
    df.dropna(subset = [field_to_plot], inplace=True) #drop null values
    df.index = range(0,len(df))

    y = df["long_LKS94"]
    x = df["lat_LKS94"]
    z = df[field_to_plot]

    X, Y, Z = interpolate_XYZ(x, y, z, resolution=50, contour_method='cubic')

    sns.color_palette(colormap, as_cmap=True)
    contour_step_count = 25
    plt.contourf(X, Y, Z, contour_step_count, cmap=colormap)
    plt.clim(vmin=z.min(), vmax=z.max())
    plt.colorbar(shrink=0.8)
    plt.autoscale(False)
    plt.xticks([])
    plt.yticks([])

    print("\n")




def result_directory_cleanup(folder):
    print("---------------- DELETE OLD REPORT ----------------")
    import os, shutil
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print("\n")




print("#################### PROCESS ####################")

date = '2021-11-29'
time = '16:30'
time_oldest_allowed = datetime.strptime(time, '%H:%M') - datetime.strptime("00:15", '%H:%M')
result_dir = './reports/'

df = get_weather_data(date,time)

subplot_count = 5

plt.style.use('dark_background')
plt.figure(figsize=(10,subplot_count*7))

plt.subplot(subplot_count,1,1)
plot_as_surface(df,'air_temp_C','coolwarm')
add_LTUBorder_layer(LTU_x, LTU_y)
add_station_layer(df)
add_statistics(df,'air_temp_C')
add_name('Air temperature [C]')

plt.subplot(subplot_count,1,2)
plot_as_surface(df,'wind_spd_avg_ms','Purples')
add_LTUBorder_layer(LTU_x, LTU_y)
add_station_layer(df)
add_statistics(df,'wind_spd_avg_ms')
add_name('Wind speed [m/s]')

plt.subplot(subplot_count,1,3)
plot_as_surface(df,'wind_spd_max_ms','Reds')
add_LTUBorder_layer(LTU_x, LTU_y)
add_station_layer(df)
add_statistics(df,'wind_spd_max_ms')
add_name('Wind gusts [m/s]')

plt.subplot(subplot_count, 1, 4)
plot_as_surface(df,'prcp_amount_mm','Blues')
add_LTUBorder_layer(LTU_x, LTU_y)
add_station_layer(df)
add_statistics(df,'prcp_amount_mm')
add_name('Precipitation intensity [mm/h]')

plt.subplot(subplot_count, 1, 5)
plot_as_surface(df,'visibility_m','Blues')
add_LTUBorder_layer(LTU_x, LTU_y)
add_station_layer(df)
add_statistics(df,'visibility_m')
add_name('Visibility [m]')

plt.tight_layout()
result_directory_cleanup(result_dir)

print("---------------- SAVE NEW REPORT ----------------")
plt.savefig(result_dir+'Report.png', dpi=200, orientation='portrait')


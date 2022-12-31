import os
import pandas as pd
import proj2proj_CY as p2p

# pathO = 'D:\\programmer_\\cgsNE_basemap_CY\\'

pathO = os.getcwd()
data = pathO + "\\0_raw_frKD\\line_XY_3c.dat"

def UTM50N2degdecimal(df):
    '''
    UTM50N converting to lon&lat(degreeOfDecimal) by using segy2segy
    '''
    lon=df["x_coor"].values.tolist()
    lat=df["y_coor"].values.tolist()

    return p2p.segy2segy(s_srs=32650, t_srs=4326, X=lon, Y=lat)



df = pd.read_csv(data, sep=",", header=None)
df.set_axis(['linename', 'trace', 'x_coor', 'y_coor'], axis='columns', inplace=True)
print(df)
# convert coor
data_ll = UTM50N2degdecimal(df)

df['lon'] = data_ll['lon']
df['lat'] = data_ll['lat']

df.to_csv(pathO + "\\1_XY_ll\\line_XY_ll.csv")
print(data_ll)
from operator import index
import os


pathO = os.getcwd()
data = pathO + "/1_XY_ll/line_XY_ll.csv"

linename = []
lon = []
lat = []
with open(data) as f:
    lines = f.readlines()
    for i in range(0, len(lines), 1):
        if(i != 0):
            s = lines[i].split(',')
            linename.append(str(s[1]).strip().replace('/', '_'))
            lon.append(str(s[5]).strip())
            lat.append(str(s[6]).strip())

unique = []
for lname in linename:
    if lname not in unique:
        unique.append(lname)

# split and save
for lname in unique:
    path = pathO + '/2_XY_ll_splited/' + lname + '.csv'
    f = open(path, 'w')
    f.write('linename' + ',' + 'lon' + ',' + 'lat' + '\n')

    for i in range(0, len(lon), 1):
        if linename[i] == lname:
            f.write(linename[i] + ',' + lon[i] + ',' + lat[i] + '\n')
    
    f.close()
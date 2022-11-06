# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:12:59 2022

@author: vaugh
"""


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from math import radians, sin, cos, acos

def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 3958.756 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )

def lowest_coordinate(cor1, cor2):
    if cor1 <= cor2:
        return cor1
    else:
        return cor2
    
def highest_coordinate(cor1, cor2):
    if cor1 >= cor2:
        return cor1
    else:
        return cor2    

def percent_expansion(number, perc):
    per = number/100*perc+number
    return per

def cordistance(cor1, cor2):
    if cor1 < 0 and cor2 >= 0:
        cord1 = cor1 + 180
        if cord1 > cor2:
            length = cord1 - cor2
        elif cor1 == cor2:
            length = cord1
        else:
            length = cor2 - cord1
    elif cor2 < 0 and cor1 >= 0:
        cord2 = cor2 + 180
        if cor1 > cord2:
            length = cor1 - cord2
        elif cor1 == cord2:
            length = cor1
        else:
            length = cord2 - cor1
    elif cor1 >= 0 and cor2 >= 0:
        if cor1 > cor2:
            length = cor1 - cor2
        elif cor1 == cor2:
            length = cor1
        else:
            length = cor2 - cor1
    elif cor1 < 0 and cor2 < 0:
        if cor1 > cor2:
            length = cor1 - cor2
        elif cor1 == cor2:
            length = cor1
        else:
            length = cor2 - cor1
    return length


def scale_map(lat1, lon1, lat2, lon2):
    cd1=cordistance(lat1, lat2)
    cd2=cordistance(lon1, lon2)
    if cd1 > cd2:
        perc=(cd1/cd2)/3+10
        llcrln=percent_expansion(lowest_coordinate(lon1, lon2), perc)
        urcrln=percent_expansion(highest_coordinate(lon1, lon2), perc)
        llcrlt=percent_expansion(lowest_coordinate(lat1, lat2), 10)
        urcrlt=percent_expansion(highest_coordinate(lat1, lat2), 10)
        return llcrln, llcrlt, urcrln, urcrlt
    elif cordistance(lat1, lat2) < cordistance(lon1, lon2):
        perc=(cd2/cd1)/2+10
        llcrln=percent_expansion(lowest_coordinate(lon1, lon2), 10)
        urcrln=percent_expansion(highest_coordinate(lon1, lon2), 10)
        llcrlt=percent_expansion(lowest_coordinate(lat1, lat2), perc)
        urcrlt=percent_expansion(highest_coordinate(lat1, lat2), perc)
        return llcrln, llcrlt, urcrln, urcrlt
    else:
        pass

def data_retrieve(country1, city1, lon1, lat1, pop1, country2, city2, lon2, lat2, pop2):
    a1=[country1, city1, lon1, lat1, pop1]
    a2=[country2, city2, lon2, lat2, pop2]
    return a1, a2
    
a1, a2 = data_retrieve('Germany', 'Munich', 11.5820, 48.1351, 1472000, 'Germany', 'Bremen', 8.8017, 53.0793, 569352)

name1 = a1[1]
lat1 = a1[3]
lon1 = a1[2]
pop1 = a1[4]
name2 = a2[1]
lat2 = a2[3]
lon2 = a2[2]
pop2 = a2[4]


#Find central lon
cenlon = (lon1+lon2)/2
#Find central lat
cenlat = (lat1+lat2)/2

#distance between points
distance = great_circle(lon1, lat1, lon2, lat2)

# create new figure, axes instances.
fig=plt.figure(figsize=(5,5))
ax=fig.add_axes([0.1,0.1,0.8,0.8])
res='l'
# setup mercator map projection.
wth=distance*4314
hht=distance*2486
m = Basemap(width=wth,height=hht,
            resolution=res,projection='tmerc', 
            lon_0=cenlon,lat_0=cenlat)

# draw great circle route
m.drawgreatcircle(lon1,lat1,lon2,lat2,linewidth=2,color='r',alpha=0.8)
#map type
m.shadedrelief()

#Population
'''
lons = [lon1, lon2]
lats = [lat1, lat2]
pops = [pop1, pop2]
area = [area1, area2]
m.scatter(lons, lats, latlon=True,
          c=np.log10(pops), s=area,
          cmap='Reds', alpha=0.5)
plt.colorbar(0.5, 0.5,label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)
for a in [100, 300, 500, 700]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1.3, loc='lower left');
'''

plt.title('Distance: {:.2f} km'.format(distance))

plt.show()
plt.savefig('map.jpg')
plt.close()

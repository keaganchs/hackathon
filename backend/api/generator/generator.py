# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:12:59 2022

@author: vaugh
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from math import radians, sin, cos, acos
import numpy as np

def generate_map_figure(lon1, lat1, pop1, lon2, lat2, pop2):

    def great_circle(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        
        return 3958.756 * (
            acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
        )

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
    lons = [lon1, lon2]
    lats = [lat1, lat2]
    pops = [pop1, pop2]
    area = [pop1/10000, pop2/10000]
    m.scatter(lons, lats, latlon=True,
            c=np.log10(pops), s=area,
            cmap='Reds', alpha=0.5)
    plt.colorbar(label=r'$\log_{10}({\rm population})$', orientation = 'horizontal')
    plt.clim(3, 7)


    plt.title('Distance: {:.2f} km'.format(distance))

    #plt.show()
    plt.savefig('map.png')
    plt.close()
    
    return fig

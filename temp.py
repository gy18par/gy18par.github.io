# -*- coding: utf-8 -*-
"""
Created on Fri June 21 17:07:39 2019

@author: gy18par
"""

# This Python script is one example of how algorithm testing can be automated 
# and used in conjunction with ArcMap for the extraction of surface water features
# namely, the Rio Doce netowrk in Brazil.

# start

#import functions
import os                                                   # working directory
from osgeo import gdal
from osgeo.gdalconst 

# Get working directory 
os.getcwd()

# Choose the driver type
driver = gdal.GetDriverByName('GTiff')

# Import imagery and/ or data type
filename = 'data/LC81980242014260LGN00_sr_band4.tif'       # Landsat 8 examples
filename = 'data/LC81980242014260LGN00_sr_band5.tif'

# Make arrays of the input data
band4Arr = dataSource4.ReadAsArray(0,0,dataSource4.RasterXSize, dataSource4.RasterYSize)
band5Arr = dataSource5.ReadAsArray(0,0,dataSource5.RasterXSize, dataSource5.RasterYSize)

# Convert files to float
import numpy as np
band4Arr=band4Arr.astype(np.float32)
band5Arr=band5Arr.astype(np.float32)

# Calculating NDWI 
mask = np.greater(band4Arr+band5Arr,0)
NDWI = np.choose(mask,(-99,(band4Arr-band5Arr)/(band4Arr+band5Arr)))

# Extract information about NDWI values
print "max min mean NDWI"
print NDWI.max()
print NDWI.min()
print NDWI.mean()

# Create .tif output file
outDataSet=driver.Create('data/NDWI.tif')
outBand = outDataSet.GetRasterBand(1)
outBand.WriteArray(NDWI,0,0)
outBand.SetNoDataValue(-99)

# Set projection
outDataSet.SetProjection(dataSource4.GetProjection())

# end
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
import numpy as np 

# Get working directory 
os.getcwd()

# Choose the driver type
driver = gdal.GetDriver('GTiff')

# Import imagery and/ or data type
filename = 'data/LC81980242014260LN654_sr_band4.tif'       # Landsat 8 examples
filename = 'data/LC81980242014260LN654_sr_band7.tif'

# Make arrays of the input data
band4Arr = dataSource.ReadAsArray(0,0,dataSource.RasterXSize)
band5Arr = dataSource.ReadAsArray(0,0,dataSource.RasterYSize)

# Convert files to float
band4Arr=band4Arr.astype(np.float)
band7Arr=band7Arr.astype(np.float)

# Calculating NDWI 
mask = np.greater(bandArr+bandArr,0)
NDWI = np.choose(mask,(-99,(band4Arr-band7Arr)/(band4Arr+band7Arr)))

# Extract information about NDWI values
print NDWI.max()
print NDWI.min()
print NDWI.mean()

# Create .tif output file
outData.Create('data/NDWI.tif')
outBand = outDataSet.GetRaster
outBand.WriteArray(NDWI,0,0)
outBand.SetNoDataValue(-99)

# Set projection
outDataSet.SetProjection(dataSource.GetProjection())

# end
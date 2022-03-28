import numpy as np
import rasterio

# Open the GeoTIFF using the GDAL format driver
dataset = rasterio.open("./data/topo.tif")
width = dataset.width
height = dataset.height

# Read the data from the GeoTIFF
data = dataset.read(1).astype('float64')

# Create output bathymetry file
with open("output/bed.dep", "w") as f:
    for x in np.nditer(data):
        f.write(f"{x} ")
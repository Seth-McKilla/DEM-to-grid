import numpy as np
import rasterio

# Open the GeoTIFF using the GDAL format driver
dataset = rasterio.open("./data/topo.tif")
width = dataset.width
height = dataset.height

# Read the data from the GeoTIFF
data = dataset.read(1).astype("float")
data = np.round(data, 6)  # Convert to meters and set precision
data[(data < -1e10) | (data > 1e10)] = 0  # Set nodata values to 0

# Create output bathymetry file
counter = 0

with open("output/bathy.dep", "w") as f:
    print("Writing output bathymetry file...")
    for x in np.nditer(data):
        if counter == width:
            f.write("\n")
            counter = 0

        f.write(f"{x} ")
        counter += 1
    print("Done!")

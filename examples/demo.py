import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import rasterio
from rasterio.transform import from_origin
import matplotlib.pyplot as plt
from src.analysis import analyze_scene
from src.visualize import plot_results

def create_dummy_raster(path: str, mean_val: float, size: int = 100):
    """Creates a dummy single-band GeoTIFF."""
    # Create random data with some structure
    data = np.random.normal(mean_val, 0.1, (size, size)).astype('float32')
    
    # Add a "mineral anomaly" patch in the center
    center = size // 2
    if 'B04' in path: # Red high
        data[center-10:center+10, center-10:center+10] += 0.5
    if 'B02' in path: # Blue low
        data[center-10:center+10, center-10:center+10] -= 0.2
    
    # Add a "vegetation" patch
    if 'B08' in path: # NIR high
        data[10:30, 10:30] += 0.8
    if 'B04' in path: # Red low
        data[10:30, 10:30] -= 0.5
    
    # Add a "water" patch
    if 'B03' in path: # Green high
        data[70:90, 10:30] += 0.4
    if 'B08' in path: # NIR low
        data[70:90, 10:30] -= 0.6
        
    transform = from_origin(300000, 4000000, 10, 10) # Dummy coords
    
    with rasterio.open(
        path, 'w', driver='GTiff',
        height=size, width=size,
        count=1, dtype=data.dtype,
        crs='+proj=latlong',
        transform=transform,
    ) as dst:
        dst.write(data, 1)

def main():
    print("🧪 Generative Synthetic Sentinel-2 Data...")
    os.makedirs('examples/data', exist_ok=True)
    
    # Create dummy bands
    bands_config = {
        'B02': 0.3, # Blue
        'B03': 0.4, # Green
        'B04': 0.3, # Red
        'B08': 0.4, # NIR
        'B11': 0.2, # SWIR1
        'B12': 0.15 # SWIR2
    }
    
    paths = {}
    for band, mean in bands_config.items():
        p = f'examples/data/{band}.tif'
        create_dummy_raster(p, mean)
        paths[band] = p
        
    print("⚙️  Running Analysis Pipeline (Veg & Water Masking enabled)...")
    results = analyze_scene(paths, mask_vegetation=True, mask_water_bodies=True)
    
    output = 'examples/demo_output.png'
    plot_results(results, output_path=output)
    print(f"✨ Demo Complete! Check {output}")

if __name__ == "__main__":
    main()

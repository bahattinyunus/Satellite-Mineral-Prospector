import sys
import os
import numpy as np

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analysis import analyze_scene
from src.visualize import plot_results, plot_3d_prospectivity
from src.exporter import export_to_geotiff
from examples.demo import create_dummy_raster

def main():
    print("💎 Satellite Mineral Prospector: MASTERCLASS DEMO 💎")
    os.makedirs('examples/masterclass_data', exist_ok=True)
    
    # 1. Generate Complex Synthetic Data
    bands_config = {
        'B02': 0.3, 'B03': 0.4, 'B04': 0.3,
        'B08': 0.4, 'B11': 0.2, 'B12': 0.15
    }
    
    paths = {}
    for band, mean in bands_config.items():
        p = f'examples/masterclass_data/{band}.tif'
        create_dummy_raster(p, mean, size=150)
        paths[band] = p
        
    # 2. Run Intelligent Analysis (AI + Physical)
    print("\n🔍 Running Intelligent Analysis Pipeline...")
    results = analyze_scene(paths, mask_vegetation=True, mask_water_bodies=True)
    
    # 3. GeoTIFF Export (Professional Standard)
    print("\n🌍 Exporting Professional GeoTIFF...")
    export_to_geotiff('examples/masterclass_analysis.tif', results, paths['B02'])
    
    # 4. 3D Visual Mapping
    print("\n🏔️ Generating 3D Prospectivity Map...")
    plot_3d_prospectivity(results, index_name='lithium_prospect', output_path='examples/lithium_3d.png')
    
    # 5. Summary Visualization
    print("\n📊 Generating Summary Dashboard...")
    plot_results(results, output_path='examples/masterclass_dashboard.png')
    
    print("\n✨ Masterclass Integration Complete! All modules verified.")

if __name__ == "__main__":
    main()

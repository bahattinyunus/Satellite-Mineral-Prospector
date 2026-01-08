import rasterio
import numpy as np
from typing import Dict, Any, Optional

def export_to_geotiff(output_path: str, results: Dict[str, np.ndarray], reference_path: str):
    """
    Exports multiple indices to a single multi-band GeoTIFF with full spatial metadata.
    
    Args:
        output_path (str): Final file path (.tif).
        results (Dict[str, np.ndarray]): Dictionary of result maps.
        reference_path (str): Path to an original band file to copy profile metadata from.
    """
    with rasterio.open(reference_path) as src:
        profile = src.profile.copy()
        
    names = sorted([k for k in results.keys() if isinstance(results[k], np.ndarray)])
    num_bands = len(names)
    
    # Update profile for output
    profile.update(
        dtype=rasterio.float32,
        count=num_bands,
        nodata=np.nan,
        driver='GTiff'
    )
    
    with rasterio.open(output_path, 'w', **profile) as dst:
        for i, name in enumerate(names, start=1):
            data = results[name].astype(rasterio.float32)
            dst.write(data, i)
            dst.set_band_description(i, name)
            
    print(f"🌍 Professional GeoTIFF exported to: {output_path}")

def save_metadata(output_path: str, metadata: Dict[str, Any]):
    """
    Saves logical metadata for the analysis session.
    """
    import json
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)

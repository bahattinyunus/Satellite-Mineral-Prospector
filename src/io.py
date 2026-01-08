import rasterio
import numpy as np
from typing import Tuple, Dict

def read_band(filepath: str) -> np.ndarray:
    """
    Reads a single raster band from a file.
    
    Args:
        filepath (str): Path to the raster file.
    
    Returns:
        np.ndarray: The band data as a numpy array (float32).
    """
    with rasterio.open(filepath) as src:
        # Read the first band
        band_data = src.read(1).astype('float32')
        
        # Handle nodata if present (converts to NaN or keeping it for masking later)
        if src.nodata is not None:
             band_data[band_data == src.nodata] = np.nan
             
    return band_data

def get_metadata(filepath: str) -> Dict:
    """
    Returns the metadata of a raster file (profile).
    """
    with rasterio.open(filepath) as src:
        return src.profile

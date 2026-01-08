import numpy as np
from src.indices import ndvi

def create_vegetation_mask(nir_band: np.ndarray, red_band: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """
    Creates a boolean mask for vegetation using NDVI.
    True indicates vegetation (to be masked out or handled).
    
    Args:
        nir_band (np.ndarray): Near-Infrared band.
        red_band (np.ndarray): Red band.
        threshold (float): NDVI threshold for vegetation (default 0.3).
    
    Returns:
        np.ndarray: Boolean mask where True is vegetation.
    """
    ndvi_val = ndvi(nir_band, red_band)
    return ndvi_val > threshold

def mask_water(blue_band: np.ndarray, nir_band: np.ndarray, threshold: float = 1.0) -> np.ndarray:
     """
     Simple water masking. (Typically Water has low reflectance in NIR compared to Blue/Green, 
     but NDWI is better. Let's use a placeholder simple logic or NDWI if needed).
     For now, we will stick to a placeholder that returns False (no mask) unless requested.
     """
     return np.zeros_like(blue_band, dtype=bool)

def clean_data(band_data: np.ndarray, mask: np.ndarray, fill_value: float = np.nan) -> np.ndarray:
    """
    Applies a mask to the data, setting masked values to fill_value.
    
    Args:
        band_data (np.ndarray): Logic data.
        mask (np.ndarray): Boolean mask (True values are filled).
        fill_value (float): Value to fill.
    
    Returns:
        np.ndarray: Cleaned data.
    """
    out = band_data.copy()
    out[mask] = fill_value
    return out

import numpy as np
from src.indices import ndvi, ndwi

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

def mask_water(green_band: np.ndarray, nir_band: np.ndarray, threshold: float = 0.0) -> np.ndarray:
    """
    Creates a boolean mask for water using NDWI.
    Args:
        green_band (np.ndarray): Green band (B03 in Sentinel-2).
        nir_band (np.ndarray): NIR band (B08 in Sentinel-2).
        threshold (float): NDWI threshold (default 0.0 for deep water).
    Returns:
        np.ndarray: Boolean mask where True is water.
    """
    ndwi_val = ndwi(green_band, nir_band)
    return ndwi_val > threshold

def apply_auto_contrast(data: np.ndarray, lower_percentile: float = 2, upper_percentile: float = 98) -> np.ndarray:
    """
    Applies simple percentile-based contrast stretching.
    """
    non_nan = data[~np.isnan(data)]
    if non_nan.size == 0:
        return data
    
    p_low, p_high = np.percentile(non_nan, [lower_percentile, upper_percentile])
    stretched = np.clip(data, p_low, p_high)
    # Normalize to 0-1
    return (stretched - p_low) / (p_high - p_low + 1e-6)

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

import numpy as np
from typing import Dict, List
from src.io import read_band
from src.indices import iron_oxide, clay_minerals, ferrous_minerals, ndvi
from src.preprocessing import create_vegetation_mask, clean_data

def analyze_scene(band_paths: Dict[str, str], mask_vegetation: bool = True) -> Dict[str, np.ndarray]:
    """
    Performs full spectral analysis on a scene.
    
    Args:
        band_paths (Dict[str, str]): Dictionary mapping band names ('B02', 'B04', etc.) to file paths.
        mask_vegetation (bool): Whether to mask out high vegetation areas.
        
    Returns:
        Dict[str, np.ndarray]: Dictionary of result maps ('iron_oxide', 'clay', etc.).
    """
    # Load required bands
    # Sentinel-2 Scheme:
    # B02: Blue
    # B04: Red
    # B08: NIR
    # B11: SWIR1
    # B12: SWIR2
    
    b02 = read_band(band_paths['B02'])
    b04 = read_band(band_paths['B04'])
    b08 = read_band(band_paths['B08'])
    b11 = read_band(band_paths['B11'])
    b12 = read_band(band_paths['B12'])
    
    results = {}
    
    # Calculate Mask
    mask = None
    if mask_vegetation:
        mask = create_vegetation_mask(b08, b04)
        results['vegetation_mask'] = mask
        
    # Calculate Indices
    io_map = iron_oxide(b04, b02)
    clay_map = clay_minerals(b11, b12)
    ferrous_map = ferrous_minerals(b12, b08)
    
    # Apply Mask
    if mask is not None:
        io_map = clean_data(io_map, mask)
        clay_map = clean_data(clay_map, mask)
        ferrous_map = clean_data(ferrous_map, mask)
        
    results['iron_oxide'] = io_map
    results['clay_minerals'] = clay_map
    results['ferrous_minerals'] = ferrous_map
    
    return results

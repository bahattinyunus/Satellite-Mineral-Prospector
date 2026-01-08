import numpy as np
from typing import Dict, List
from src.io import read_band
from src.indices import iron_oxide, clay_minerals, ferrous_minerals, ndvi, lithium_index, gossan_index
from src.preprocessing import create_vegetation_mask, mask_water, clean_data, apply_auto_contrast
from src.ai_classifier import detect_spectral_anomalies

def analyze_scene(band_paths: Dict[str, str], mask_vegetation: bool = True, mask_water_bodies: bool = True) -> Dict[str, np.ndarray]:
    """
    Performs full spectral analysis on a scene.
    
    Args:
        band_paths (Dict[str, str]): Dictionary mapping band names ('B02', 'B03', 'B04', etc.) to file paths.
        mask_vegetation (bool): Whether to mask out high vegetation areas.
        mask_water_bodies (bool): Whether to mask out water bodies using NDWI.
        
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
    b03 = read_band(band_paths['B03'])
    b04 = read_band(band_paths['B04'])
    b08 = read_band(band_paths['B08'])
    b11 = read_band(band_paths['B11'])
    b12 = read_band(band_paths['B12'])
    
    results = {}
    
    # Calculate Mask
    combined_mask = np.zeros_like(b02, dtype=bool)
    if mask_vegetation:
        veg_mask = create_vegetation_mask(b08, b04)
        combined_mask |= veg_mask
        results['vegetation_mask'] = veg_mask
    
    if mask_water_bodies:
        w_mask = mask_water(b03, b08)
        combined_mask |= w_mask
        results['water_mask'] = w_mask
        
    # Calculate Indices
    io_map = iron_oxide(b04, b02)
    clay_map = clay_minerals(b11, b12)
    ferrous_map = ferrous_minerals(b12, b08)
    li_map = lithium_index(b11, b12, b02)
    gs_map = gossan_index(b11, b04)
    
    # Apply Mask and Auto-Contrast
    index_maps = {
        'iron_oxide': io_map,
        'clay_minerals': clay_map,
        'ferrous_minerals': ferrous_map,
        'lithium_prospect': li_map,
        'gossan_detection': gs_map
    }
    
    for name, data in index_maps.items():
        cleaned = clean_data(data, combined_mask)
        results[name] = apply_auto_contrast(cleaned)
    
    # AI Anomaly Detection
    print("🤖 Running AI Anomaly Detection...")
    results['ai_anomalies'] = detect_spectral_anomalies(results)
        
    return results

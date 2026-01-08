import numpy as np

def calculate_index(band1: np.ndarray, band2: np.ndarray, epsilon: float = 1e-6) -> np.ndarray:
    """
    Generic safe division for spectral indices.
    Args:
        band1 (np.ndarray): Numerator band.
        band2 (np.ndarray): Denominator band.
        epsilon (float): Small value to avoid division by zero.
    Returns:
        np.ndarray: Calculated index.
    """
    return (band1) / (band2 + epsilon)

def normalized_difference(band1: np.ndarray, band2: np.ndarray, epsilon: float = 1e-6) -> np.ndarray:
    """
    Calculates Normalized Difference Index: (B1 - B2) / (B1 + B2)
    """
    return (band1 - band2) / (band1 + band2 + epsilon)

def iron_oxide(red_band: np.ndarray, blue_band: np.ndarray) -> np.ndarray:
    """
    Calculates Iron Oxide Index (Red / Blue).
    Identify limonite-bearing zones.
    Sentinel-2: B4 / B2
    """
    return calculate_index(red_band, blue_band)

def clay_minerals(swir1_band: np.ndarray, swir2_band: np.ndarray) -> np.ndarray:
    """
    Calculates Clay Minerals Index (SWIR1 / SWIR2).
    Identify hydroxyl-bearing minerals (clays, micas).
    Sentinel-2: B11 / B12
    """
    return calculate_index(swir1_band, swir2_band)

def ferrous_minerals(swir_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """
    Calculates Ferrous Minerals Index (SWIR / NIR).
    Sentinel-2: B12 / B8 (Simple Ratio approximation)
    """
    return calculate_index(swir_band, nir_band)

def ndvi(nir_band: np.ndarray, red_band: np.ndarray) -> np.ndarray:
    """
    Normalized Difference Vegetation Index.
    Useful for masking out vegetation to avoid false positives.
    Sentinel-2: (B8 - B4) / (B8 + B4)
    """
    return normalized_difference(nir_band, red_band)

def ndwi(green_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """
    Normalized Difference Water Index.
    Used to monitor changes related to water content in water bodies.
    Sentinel-2: (B3 - B8) / (B3 + B8)
    """
    return normalized_difference(green_band, nir_band)

def lithium_index(swir1_band: np.ndarray, swir2_band: np.ndarray, blue_band: np.ndarray) -> np.ndarray:
    """
    Experimental Lithium Index for brine/pegmatite detection.
    (SWIR1 / SWIR2) * (Blue) approximation.
    """
    # Simplified approximation for pegmatite/brine contrast
    ratio = calculate_index(swir1_band, swir2_band)
    return ratio * blue_band

def gossan_index(swir1_band: np.ndarray, red_band: np.ndarray) -> np.ndarray:
    """
    Gossan Detection Index.
    Identifies weathered rock containing iron oxides (often above sulfide deposits).
    Sentinel-2: B11 / B4
    """
    return calculate_index(swir1_band, red_band)

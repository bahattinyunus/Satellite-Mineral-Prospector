import numpy as np
from sklearn.ensemble import IsolationForest
from typing import Dict, Optional

def detect_spectral_anomalies(index_maps: Dict[str, np.ndarray], contamination: float = 0.05) -> np.ndarray:
    """
    Uses Isolation Forest to detect unsupervised spectral anomalies across multiple mineral indices.
    
    Args:
        index_maps (Dict[str, np.ndarray]): Dictionary of calculated mineral indices (iron, clay, etc.).
        contamination (float): The amount of contamination of the data set, i.e. the proportion 
                             of outliers in the data set.
                             
    Returns:
        np.ndarray: A boolean mask where True indicates an anomaly (potential mineral target).
    """
    # Flatten and stack all indices into a feature matrix
    features = []
    keys = sorted(index_maps.keys())
    shape = next(iter(index_maps.values())).shape
    
    for key in keys:
        # Handle NaNs by replacing them with 0 (or mean) for the ML model
        data = index_maps[key].flatten()
        data = np.nan_to_num(data, nan=0.0)
        features.append(data)
    
    X = np.column_stack(features)
    
    # Fit Isolation Forest
    clf = IsolationForest(contamination=contamination, random_state=42, n_jobs=-1)
    # -1 for outliers, 1 for inliers
    preds = clf.fit_predict(X)
    
    # Reshape back to original image dimensions
    anomaly_mask = (preds == -1).reshape(shape)
    
    return anomaly_mask

def classify_mineral_zones(index_maps: Dict[str, np.ndarray], anomaly_mask: np.ndarray) -> np.ndarray:
    """
    Assigns pseudo-labels to detected anomalies based on which index is dominant.
    """
    # Placeholder for a more complex clustering/classification logic
    # Higher value = higher confidence mineral zone
    confidence_map = np.zeros(anomaly_mask.shape)
    
    for name, data in index_maps.items():
        # Normalized confidence based on index intensity within anomalous zones
        if name in ['iron_oxide', 'clay_minerals', 'lithium_prospect', 'gossan_detection']:
            confidence_map[anomaly_mask] += data[anomaly_mask]
            
    return confidence_map

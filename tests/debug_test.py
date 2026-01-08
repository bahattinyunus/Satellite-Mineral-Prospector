import numpy as np
import sys
import os

# Add current dir to path
sys.path.append(os.getcwd())

from src.indices import calculate_index, iron_oxide, ndvi

def debug():
    print("Testing calculate_index...")
    b1 = np.array([10.0, 20.0])
    b2 = np.array([2.0, 4.0])
    result = calculate_index(b1, b2)
    print(f"Result: {result}")
    
    # Check Iron Oxide
    print("Testing Iron Oxide...")
    red = np.array([100.0, 200.0])
    blue = np.array([50.0, 100.0])
    io = iron_oxide(red, blue)
    print(f"Iron Oxide: {io}")
    
    # Check NDVI
    print("Testing NDVI...")
    nir = np.array([0.5, 0.8])
    red_b = np.array([0.1, 0.1])
    ndvi_val = ndvi(nir, red_b)
    print(f"NDVI: {ndvi_val}")
    
    expected_ndvi = (nir - red_b) / (nir + red_b)
    print(f"Expected NDVI: {expected_ndvi}")

if __name__ == "__main__":
    debug()

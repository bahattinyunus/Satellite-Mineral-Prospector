import numpy as np
import pytest
from src.indices import calculate_index, iron_oxide, ndvi

def test_calculate_index():
    b1 = np.array([10.0, 20.0])
    b2 = np.array([2.0, 4.0])
    # Match the implementation's epsilon
    epsilon = 1e-6
    result = calculate_index(b1, b2, epsilon=epsilon)
    expected = b1 / (b2 + epsilon)
    np.testing.assert_array_almost_equal(result, expected)

def test_ndvi():
    nir = np.array([0.5, 0.8])
    red = np.array([0.1, 0.1])
    epsilon = 1e-6
    result = ndvi(nir, red, epsilon=epsilon)
    expected = (nir - red) / (nir + red + epsilon)
    np.testing.assert_array_almost_equal(result, expected)
    
def test_iron_oxide():
    red = np.array([100.0, 200.0])
    blue = np.array([50.0, 100.0])
    epsilon = 1e-6
    result = iron_oxide(red, blue)
    expected = red / (blue + epsilon)
    np.testing.assert_array_almost_equal(result, expected)

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Optional

def plot_results(results: Dict[str, np.ndarray], output_path: Optional[str] = None):
    """
    Plots the mineral maps.
    """
    keys = [k for k in results.keys() if 'mask' not in k]
    n = len(keys)
    
    fig, axes = plt.subplots(1, n, figsize=(5*n, 5))
    if n == 1:
        axes = [axes]
        
    for ax, key in zip(axes, keys):
        data = results[key]
        im = ax.imshow(data, cmap='viridis')
        ax.set_title(key.replace('_', ' ').title())
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        ax.axis('off')
        
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300)
    else:
        plt.show() # Note: This might not show in headless env

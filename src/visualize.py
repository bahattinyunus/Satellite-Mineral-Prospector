import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from typing import Dict, Optional

def plot_3d_prospectivity(results: Dict[str, np.ndarray], index_name: str = 'iron_oxide', output_path: str = '3d_map.png'):
    """
    Creates a pseudo-3D prospectivity map. 
    The intensity of the mineral index is used as the 'elevation'.
    """
    data = results[index_name]
    # Resize data for better 3D plotting performance if too large
    if data.shape[0] > 100 or data.shape[1] > 100:
         step_y = max(1, data.shape[0] // 100)
         step_x = max(1, data.shape[1] // 100)
         data_small = data[::step_y, ::step_x]
    else:
         data_small = data

    h, w = data_small.shape
    x = np.arange(0, w, 1)
    y = np.arange(0, h, 1)
    X, Y = np.meshgrid(x, y)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Use index intensity as Z
    surf = ax.plot_surface(X, Y, data_small, cmap='magma', edgecolor='none', alpha=0.9)
    
    ax.set_title(f'3D Mineral Prospectivity: {index_name}')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"🏔️  3D Map saved to: {output_path}")

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
        plt.show()

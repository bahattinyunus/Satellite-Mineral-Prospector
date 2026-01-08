import os
import concurrent.futures
from typing import List, Dict, Any
from src.analysis import analyze_scene
from src.exporter import export_to_geotiff

def process_single_scene(scene_config: Dict[str, Any]):
    """
    Worker function to process a single scene.
    """
    try:
        bands = scene_config['bands']
        output_path = scene_config['output_path']
        ref_band = bands['B02'] # Use B02 as reference
        
        print(f"🚀 Processing scene: {scene_config['name']}")
        results = analyze_scene(bands)
        
        # Export to GeoTIFF
        export_to_geotiff(output_path, results, ref_band)
        return {"name": scene_config['name'], "status": "success"}
    except Exception as e:
        return {"name": scene_config['name'], "status": "error", "message": str(e)}

def batch_process_scenes(configs: List[Dict[str, Any]], max_workers: int = 4):
    """
    Orchestrates parallel processing of multiple scenes.
    """
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_scene = {executor.submit(process_single_scene, cfg): cfg for cfg in configs}
        for future in concurrent.futures.as_completed(future_to_scene):
            results.append(future.result())
            
    return results

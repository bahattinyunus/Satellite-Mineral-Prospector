import click
import os
from typing import Dict
from src.analysis import analyze_scene
from src.visualize import plot_results

@click.command()
@click.option('--b02', required=True, type=click.Path(exists=True), help='Path to Blue Band (B02)')
@click.option('--b03', required=True, type=click.Path(exists=True), help='Path to Green Band (B03)')
@click.option('--b04', required=True, type=click.Path(exists=True), help='Path to Red Band (B04)')
@click.option('--b08', required=True, type=click.Path(exists=True), help='Path to NIR Band (B08)')
@click.option('--b11', required=True, type=click.Path(exists=True), help='Path to SWIR1 Band (B11)')
@click.option('--b12', required=True, type=click.Path(exists=True), help='Path to SWIR2 Band (B12)')
@click.option('--output', default='prospectivity_map.png', help='Output path for the result map')
@click.option('--mask/--no-mask', default=True, help='Apply vegetation masking')
@click.option('--water/--no-water', default=True, help='Apply water masking')
def main(b02, b03, b04, b08, b11, b12, output, mask, water):
    """
    Satellite Mineral Prospector CLI.
    
    Automated spectral analysis for mineral exploration using Sentinel-2 data.
    """
    click.echo(f"🛰️  Starting analysis...")
    click.echo(f"📂 Inputs: B02={os.path.basename(b02)}, B04={os.path.basename(b04)}...")
    
    bands = {
        'B02': b02,
        'B03': b03,
        'B04': b04,
        'B08': b08,
        'B11': b11,
        'B12': b12
    }
    
    try:
        results = analyze_scene(bands, mask_vegetation=mask, mask_water_bodies=water)
        
        click.echo("✅ Analysis complete. Generating map...")
        plot_results(results, output_path=output)
        
        click.echo(f"🎉 Success! Map saved to: {output}")
        
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

if __name__ == '__main__':
    main()

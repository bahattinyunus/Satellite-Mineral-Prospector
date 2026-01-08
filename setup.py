from setuptools import setup, find_packages

setup(
    name="satellite-mineral-prospector",
    version="1.0.0",
    description="Satellite Mineral Prospector: Advanced spectral analysis tool.",
    author="Bahattin Yunus Çetin",
    author_email="contact@ankasilicondynamics.com",
    packages=find_packages(),
    install_requires=[
        "rasterio>=1.3.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "geopandas>=0.13.0",
        "scikit-image>=0.21.0",
        "click>=8.1.0",
        "tqdm>=4.65.0"
    ],
    entry_points={
        "console_scripts": [
            "smp=src.cli:main",
        ],
    },
    python_requires=">=3.9",
)

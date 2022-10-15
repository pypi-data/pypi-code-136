import setuptools 

setuptools.setup(
    name="metro_integrase",
    version="0.0.3",
    author="Rootspring",
    author_email="cheesycod@outlook.com",
    description="A Python wrapper for the Metro Reviews API",
    long_description="A Python wrapper for the Metro Reviews API (https://github.com/MetroReviews)",
    packages=["metro_integrase"],
    install_requires=[
        "fastapi",
        "aiohttp",
        "pydantic",
    ]
)

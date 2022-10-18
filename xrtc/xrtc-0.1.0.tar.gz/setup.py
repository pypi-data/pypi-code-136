from setuptools import setup

setup(
    name="xrtc",
    package_dir={"": "src"},
    version="0.1.0",
    author="Delta Cygni Labs Ltd",
    url="https://xrtc.org",
    license="Apache-2.0",
    python_requires=">=3.10",
    install_requires=[
        # Read .env files to environment
        "python-dotenv >= 0.21.0",
        # Load and parse settings from environment
        "pydantic >= 1.10.2",
        # HTTP requests
        "requests >= 2.28.1"
    ],
)

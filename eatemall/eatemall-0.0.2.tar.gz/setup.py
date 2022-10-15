import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

setuptools.setup(
    name="eatemall",
    version="0.0.2",
    author="Jaskaran_Singh/Harsh_Singh",
    author_email="jaskaran_malhotra@yahoo.in",
    description="(CLI package to run the server and connect a client to play a multiplayer game!)",
    url="https://github.com/Jaskaran96/MultiplayerGame",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pygame"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={'': ['./src/assets/*.png','./src/assets/*.ttf']},
    entry_points={
        "console_scripts": [
            "eatemall-server = src.cli:runServer",
            "eatemall-client = src.cli:runClient",
        ]
    }
)
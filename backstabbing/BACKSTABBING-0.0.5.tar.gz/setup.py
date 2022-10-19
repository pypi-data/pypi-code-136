import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

setuptools.setup(
    name="BACKSTABBING",
    version="0.0.5",
    author="Nitesh_Dohre/Akshay_Pratap/Anurag_krishna",
    author_email="niteshdohre@gmail.com",
    description="(CLI package to run the server and connect a client to play a multiplayer game!)",
    url="https://github.com/momus-s/Real-time-network-multiplayer-game",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pygame"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "bs-server = src.cli:run_server",
            "bs = src.cli:run_client",
        ]
    }
)
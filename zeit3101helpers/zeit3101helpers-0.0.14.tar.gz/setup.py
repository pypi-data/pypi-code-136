from distutils.core import setup

setup(
    name="zeit3101helpers",  # How you named your package folder (MyLib)
    packages=["zeit3101helpers"],  # Chose the same as "name"
    version="0.0.14",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="ZEIT3101 Helper functions",  # Give a short description about your library
    author="Ryan Cartwright",  # Type in your name
    author_email="fryzee.cartwright@gmail.com",  # Type in your E-Mail
    url="https://github.com/System-Not-Found/ZEIT3101",  # Provide either the link to your github or to your website
    download_url="https://github.com/System-Not-Found/ZEIT3101/archive/v_01.tar.gz",  # I explain this later on
    install_requires=["pika", "stix2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
    ],
)

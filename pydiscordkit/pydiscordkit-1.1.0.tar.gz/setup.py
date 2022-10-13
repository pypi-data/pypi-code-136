import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydiscordkit',                           # should match the package folder
    packages=['pydiscordkit'],                     # should match the package folder
    version='1.1.0',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description="A Discord Automation library that doesn't use the Official Discord API",
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Sachit Ramesh',
    author_email='quantechlxxi.corp@gmail.com',
    url='https://github.com/therealcyber71/pydiscordkit', 
    project_urls = {                                # Optional
        "Issues": "https://github.com/therealcyber71/pydiscordkit/issues"
    },
    install_requires=['pyautogui'], #these are filler packages, you need to fill them with the packages your python package will require to function                 
    keywords=["automation", "discord", "pyautogui", "browser"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]

    )

import setuptools 

setuptools.setup(

    name="SystemVue", # Replace with your own username

    description="Python package for SystemVue 2023",

    version="2023.0",

    include_package_data=True,

    package_data = {'SystemVue': ['*']},

    packages= ["SystemVue"],

    classifiers=[

        "Programming Language :: Python :: 3",

    ],

    install_requires=["numpy", "pandas", "psutil"],

    python_requires='==3.10.*',

)
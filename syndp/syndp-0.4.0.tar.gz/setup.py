import setuptools



setuptools.setup(
        name = "syndp",
        version = "0.4.0",
        author = "Won Seok Jang",
        author_email = "memy85@naver.com",
        description = "Syndp is data synthesis package that leverages local differential privacy and various synthesis methods",
        long_description_content_type = "text/markdown",
        url = "https://github.com/memy85/Syndp",
        install_requires = ['pandas','numpy','matplotlib','sklearn'],
        classifiers = [
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        package_dir={"":"src"},
        packages=setuptools.find_packages(where="src"),
        python_requires=">=3.7"
        ) 

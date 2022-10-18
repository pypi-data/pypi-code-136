from setuptools import setup


def readme() -> str:
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    # Name of your project. When you publish this
    # package to PyPI, this name will be registered for you.
    name='commandsheet',  # Required

    # Version?
    version='0.1.0a1',  # Required

    # What does your project do?
    description="Display catalog of commands user uses often.",  # Optional

    # Longer description that users will see when
    # they visit your project at PyPI.
    long_description=readme(),  # Optional

    # Denotes that long description is in Markdown.
    # Valid values are: text/plain, text/x-rst or text/markdown.
    # Optional if 'long_description' is written in rst, otherwise
    # required (for plain-text and Markdown).
    long_description_content_type='text/markdown',  # Optional

    # Who owns this project?
    author='Niklas Larsson',  # Optional

    # Project owner's email
    author_email='',  # Optional

    # More info at: https://pypi.org/classifiers/
    classifiers=[  # Optional
        'License :: OSI Approved :: MIT License',
    ],

    # What does your project relate to?
    keywords='',  # Optional

    # Is your project larger than just few files?
    packages=['commandsheet'],  # Required

    # Which Python versions are supported?
    # e.g. 'pip install' will check this and refuse to install
    # the project if the version doesn't match.
    python_requires='>=3.10',  # Optional

    # Any dependencies?
    install_requires=[],  # Optional

    # Need to install, for example, man-pages that your project has?
    package_data={
        'example': ['commandsheet.ini'],
    },

    # Any executable scripts?
    entry_points={  # Optional
        "console_scripts": [
            'commandsheet = commandsheet.commandsheet:main',
        ]
    },

    # More info at: https://setuptools.pypa.io/en/latest/userguide/datafiles.html
    include_package_data=True,  # Optional

    # More info at: https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html
    zip_safe=False,  # Optional

    # Additional URLs that are relevant to your project?
    project_urls={  # Optional
        'Source': 'https://github.com/nikkelarsson/commandsheet',
    }
)

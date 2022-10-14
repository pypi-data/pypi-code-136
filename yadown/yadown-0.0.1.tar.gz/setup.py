from setuptools import setup


setup(
    name = "yadown",
    description="YADOWN: YAndex disk DOWNloader",
    version = "0.0.1",
    packages=['yadown'],
    entry_points ={
        'console_scripts': [
            'yadown = yadown.cmd:run'
        ]
    },
    license="MIT",
)

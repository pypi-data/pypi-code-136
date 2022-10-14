from os import path
from setuptools import setup, find_packages

package_name = 'bev-toolbox'
version = 0.1

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')

if __name__ == "__main__":

    print(f"Building wheel {package_name}-{version}")

    setup(
        # Metadata
        name=package_name,
        version=version,
        author="OpenPerceptionX",
        author_email="simachonghao@pjlab.org.cn",
        url="https://github.com/OpenPerceptionX/BEVPerception-Survey-Recipe",
        description="Toolbox for BEV Perception",
        long_description=long_description,
        long_description_content_type='text/markdown',
        license="Apache 2.0",
        # Package info
        packages=find_packages(exclude=('docs', 'example', 'waymo_playground', 'figs')),
        # packages=find_packages('bev_toolbox'),
        # package_dir={'': 'bev_toolbox'},
        zip_safe=False,
        install_requires=['opencv-python', 'numpy'],
        python_requires=">=3.5",
    )

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = "run with python -c 'import rats'"

setup(name='ratpy',
      version='1.1.9.9',
      description='An interpreter and visualiser of RATS files',
      author='Steve Ayrton',
      author_email='s.t.ayrton@icloud.com',
      classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.7'],
      license="BSD",
      packages=find_packages(),
      install_requires=['pandas>=1.3.3',
                        'dash>=2.0.0',
                        'plotly>=5.4.0',
                        'numpy>=1.19.5',
                        'dash_bootstrap_components>=1.0.3',
                        'beautifulsoup4>=4.9.3',
                        'pyarrow>=3.0.0',
                        'dash-uploader>=0.6.0',
                        'dash-extensions >= 0.0.70',
                        'lxml>=4.6.2'],
      python_requires='>=3.7',
      URL='https://github.com/IonGuide/ratpy',
      package_data={'': ['*.css','*.svg','*.ico','*.js']})

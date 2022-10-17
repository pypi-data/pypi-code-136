from setuptools import setup

setup(
  name = 'cluspy',         
  packages = ['cluspy'],   
  version = '0.1-alpha',      
  license='MIT',        
  description = 'Library for simulating cluster generation and computation for Measurement-Based Quantum Computation (MBQC).',   
  author = 'Emil Ostergaard',                   
  author_email = 'ee.ostergaard@gmail.com',     
  url = 'https://github.com/EmilOstergaard/cluspy',   
  download_url = 'https://github.com/EmilOstergaard/cluspy/archive/refs/tags/v0.1-alpha.tar.gz',    
  keywords = ['cluster', 'quantum', 'measurement-based quantum computation'],   
  install_requires=[            
          'numpy',
          'math',
          'scipy',
          'matplotlib',
          'mpl_toolkits',
          'cmath',
          'copy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)
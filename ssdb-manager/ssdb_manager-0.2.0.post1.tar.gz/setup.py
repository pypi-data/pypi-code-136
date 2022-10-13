from distutils.core import setup
setup(
  name = 'ssdb_manager',         # Name of package (should match folder)
  packages = ['ssdb_manager'],   # Chose the same as "name"
  version = '0.2.0.post1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Facilitates interaction between Python and SQL Server Management Studio',   # Give a short description about your library
  author = 'Tishman Speyer Data Analytics',       
  author_email = 'ts.datateam@gmail.com',      
  url = 'https://github.com/tsdatateam/ssdb_manager',   # Provide either the link to your github or to your website
  keywords = ['SQL', 'Server', 'pandas', 'Python', 'SSMS', 'Query', 'Database'],   # Keywords that define your package best
  install_requires=[            # Any package imported from pip (not standard library)
          'pandas',
          'pyodbc', 
          'sqlalchemy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)

from distutils.core import setup


long_description1 = """
                      This package can be used to classify salesmen on its performance of total sale and total unsold with
                      two different groups.

                      In easy words let's say we want to see performance (good and bad) salesman for urban market, 
                      rural market, and here we can use this package by passing a dataframe, column name of salesman id, 
                      column name of saleflag (indicating 0 for unsold and 1 for sold), column name of grouping column 
                      (having only two unique values or levels).
                      
                      By default,
                      By calling the chi_test() method we can get the Top 30 percentage and Bottom 30 percentage salesman.

                      We can change this top and bottom percentage by passing argument inside this chi_test() method.


                      We are using chi square test, a statistical method which indicates performance quality. 
                      
                      You can get the description by reading the readme.md file from my github.
                      link of github:

                      https://github.com/bhargabganguli/bhargabchipkg.git

                      Here you can find 

                      - how to install

                      - how to create object and use the method

                      - how to call the method and print the output
                    """

setup(name='bhargabchipkg',
      packages = ['bhargabchipkg'],
      version='0.1.0',
      description='helpful chi-square package for sales data',
      long_description= long_description1,
      url='https://github.com/bhargabganguli/bhargabchipkg.git',
      download_url = 'https://github.com/bhargabganguli/bhargabchipkg/archive/0.1.0.tar.gz', #FILL IN LATER
      author='Bhargab',
      author_email='bhargab.ganguli@gmail.com',
      keywords = ['chi_test',],
      license='MIT', #YOUR LICENSE HERE!

      install_requires=['pandas','numpy','scipy',],  #YOUR DEPENDENCIES HERE
  

      classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Your License Here  
        'Programming Language :: Python :: 3',    # List Python versions that you support Here  
        'Programming Language :: Python :: 3.4',
        ],
)
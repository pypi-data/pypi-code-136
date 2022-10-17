from setuptools import setup, find_packages  
  
setup(  
    classifiers = [  
        # 發展時期,常見的如下
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',  

        'Intended Audience :: Developers',  
  
        # The type of this library
        'Topic :: Software Development :: Build Tools',  
  
        # License information
        'License :: OSI Approved :: MIT License',  
  
        # Targeting Python version
        'Programming Language :: Python :: 3',  
    ],
    name= 'LisaPython',
    version='1.0.6',
    description='Simple description of LisaPython library',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://www.daniel-studio.tw/',
    author='Hung, Teng-Kuei',
    author_email='danielhorng@gmail.com',
    license='MIT',
    keywords='HungTengKuei',
    packages=find_packages(),
    install_requires=['']
)
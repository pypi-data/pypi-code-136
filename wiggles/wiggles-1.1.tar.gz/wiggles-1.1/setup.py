from setuptools import setup, find_packages


setup(
    name='wiggles',
    version='1.1',
    license='''Free to use but prohibited to copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software''',
    author="Ranit Bhowmick",
    author_email='bhowmickranitking@gmail.com',
    description='''This library makes signal processing easy ! 
A great tool for students to easily visualise and test their sigals virtually.
know more about me : https://linktr.ee/RanitBhowmick ''',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://linktr.ee/RanitBhowmick',
    download_url='https://github.com/Kawai-Senpai/wiggles',
    keywords=["Signal Processing",'Education','Discrete signal','Continuous signal','Basic signal operations'],
    install_requires=[
          'numpy','matplotlib'
          ],
)

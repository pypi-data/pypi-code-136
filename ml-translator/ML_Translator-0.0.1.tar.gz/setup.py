from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ML_Translator',
  version='0.0.1',
  description='A Docx File Translator Using ML',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ambreshrc',
  author_email='ambreshrc23@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='ML_Translator, Translator, Ambreshrc, Ambresh', 
  packages=find_packages(),
  install_requires=['sentencepiece','torch','torchvision','torchaudio','transformers','python-docx','sacremoses','nltk','tqdm'] 
)

from setuptools import setup

setup(
   name='essAI',
   version='1.0.0',
   author='Vaedz',
   author_email='dhruv.vaed@gmail.com',
   packages=['essAI Core'],
   scripts=['essAI Core/main.py'],
   description='Essay Generator',
   install_requires=[
       "torch",
       "torchvision",
       "torchaudio",
       "transformers"
   ],
)
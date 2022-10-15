from setuptools import setup, Extension


setup (name = 'pyMatrixStack',
       version = '0.0.5',
       description = 'Matrix stack for OpenGL',
       author = 'William Emerison Six',
       author_email = 'billsix@gmail.com',
       url = 'https://github.com/billsix/pyMatrixStack',
       keywords = "nuklear imgui",
       license = "MIT",
       packages=['pyMatrixStack'],
       package_dir={'pyMatrixStack': 'src/pyMatrixStack'},
       classifiers=[
           "Development Status :: 3 - Alpha",
           "Topic :: Utilities",
           "License :: OSI Approved :: MIT License",
       ],
       install_requires=[
           'numpy'],
       long_description = '''
A matrix stack implementation for OpenGL 3+
''')

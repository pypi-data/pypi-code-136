import setuptools

kubit = 'kubit'

setuptools.setup(name=kubit,
                 version="1.5.0",
                 description=kubit,
                 long_description="""This is a Jupyter Server Extension to retrieve and store a CSV
file from a URL in a pandas data frame that can be manipulated
in a Jupyter python notebook.""",
                 author='Kubit AI, Inc.',
                 author_email='info@kubit.co',
                 packages=[kubit],
                 install_requires=[
                    'nbformat==5.7.0',
                    'tornado==6.2',
                    'notebook==6.4.12',
                    'pandas==1.5.0',
                    'requests==2.28.1',
                 ],
                 license='MIT License',
                 zip_safe=False)

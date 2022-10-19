from distutils.core import setup

setup(name='denmanlab',
      version='0.1',
      description='denmanlab code, mostly for neurophysiology',
      author='denman lab',
      author_email='daniel.denman@cuanschutz.edu',
      url='https://denmanlab.github.io',
      packages= ['dlab'],
      install_requires = ['scipy', 'matplotlib', 'numpy','pandas','scikit-learn'],
     )
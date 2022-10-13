from setuptools import setup, find_packages

setup(
    name = 'ACETH',
    version = '0.0.13',
    author = 'Karim Galal, Walid Chatt',
    author_email = 'karim.galal@analytics-club.org, walid.chatt@analytics-club.org',
    license = 'MIT',
    url='https://github.com/kimo26/ACE',
    description = 'Analytics Club ETHZ helper package',
    packages=find_packages(),
    package_data={'ACETH': ['data/emoji_model.h5','data/encoder_emoji.pkl','data/token_emoji.pkl']},
    include_package_data=True,
    keywords = ['ETHZ', 'Analytics Club','AI','Artificial intelligence',
                'Machine Learning', 'Data processing','Chatbot',
                'Education','ML'],
    install_requires = [
        'numpy','pandas','torch',
        'tensorflow','transformers','sklearn',
        'emoji','accelerate','bitsandbytes','scikit-learn',
        ],
    classifiers=[
        'Programming Language :: Python :: 3'
        ]
    )

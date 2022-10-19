import setuptools

setuptools.setup(
        name='PyaiVS',
        version='1.0.4',
        description="model_bulid & vitual_screen",
        # long_description=open('README.md').read(),
        include_package_data=True,
        author='bokey',
        author_email='',
        url='',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ],
        python_requires='>=3',
        #install_requires=['rdkit==2022.03.5','pytorch==1.9.0','dgl-cuda10.2==0.4.3post2',
        #                  'deepchem==2.6.1','xgboost==1.5.1','hyperopt==0.2.7','pytorch-gpu==1.9.0','torchaudio==0.9.0 '],  # 安装所需要的库
        entry_points={
            'console_scripts': [
                ''],
        },
)

from distutils.core import setup
from setuptools import find_packages

with open('README.md', 'r', encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='pywong',
    version='3.1.5',
    description='pywong工具模块.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0 license',
    url='https://pypi.org/project/pywong/',
    packages=find_packages(),
    python_requires='>=3.8',
    platforms=['all'],
    data_files=['README.md'],
    author='ghy',
    author_email='1563713769@qq.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        # 开发的目标用户
        'Intended Audience :: Developers'
    ],
    install_requires=['PyMySQL>=1.0.2',
                      'psycopg2>=2.9.3',
                      # 'psycopg2-binary>=2.9.3',
                      'pymssql>=2.2.5',
                      'SQLAlchemy>=1.4.39',
                      'psutil>=5.9.1',
                      'scikit-learn>=1.1.1',
                      'prophet>=1.1',
                      'pyod>=1.0.4'],
    py_modules=['pywong.db.settings',
                'pywong.db.mssql.settings', 'pywong.db.mssql.utils',
                'pywong.db.mysql.settings', 'pywong.db.mysql.utils',
                'pywong.db.postgresql.settings', 'pywong.db.postgresql.utils',
                'pywong.monitor.resource_monitor',
                'pywong.ml.sk.knn', 'pywong.ml.sk.linear_regression',
                'pywong.ml.sk.random_forest', 'pywong.ml.sk.time_series',
                'pywong.ml.preprocessing.abnormal_cof',
                'pywong.app.db_tools']
)

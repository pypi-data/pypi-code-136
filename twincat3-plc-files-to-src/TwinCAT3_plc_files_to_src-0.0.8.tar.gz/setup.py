from setuptools import setup, find_packages
import subprocess
import os

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v, i, s = version.split("-")
    version = v + "+" + i + ".git." + s

#assert "-" not in version
#assert "." in version

#assert os.path.isfile("src/version.py")

print(f'\n====  Version: {version} ====\n')
with open("src/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % version)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='TwinCAT3_plc_files_to_src',
    version='0.0.8',
    description='desc',
    url='https://github.com/TobiasFreyermuth/TwinCAT3_plc_files_to_src',
    author='Tobias Freyermuth',
    author_email='Tobias.Freyermuth@posteo.net',
    license='MIT',
    python_requires='>=3.10',
    install_requires=[
        'lxml>=4.0.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10'
    ],
    py_modules=['TwinCAT3_plc_files_to_src'],
    package_dir={'': 'src'},
    packages=find_packages("src"),
    package_data={"TwinCAT3_plc_files_to_src": ["VERSION"]},
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    extras_require={
        "dev": [
            "pytest>=7.0",
        ]
    },
)
from setuptools import setup, find_packages

setup(
    name="task_master_assignment1_CMST",
    version="0.1.0",
    description="assignment 1",
    long_description="assignment 1, CMST Team",
    long_description_content_type='text/x-rst',
    url="https://gitlab.com/d_c_monti/assignment_1.git",
    author="CMST Team",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'],
    packages=find_packages(where="src"),
    python_requires='>=3',
)
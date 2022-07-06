from setuptools import find_packages, setup

setup(
    name='data-struct',
    packages=find_packages('src.data_struct'),
    package_dir={'': 'src'},
    version='0.1.0',
    description='Data Structure and Algorithms',
    author='ming_gao@outlook.com',
    license='MIT',
)
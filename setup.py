import glob
import os
import sys
from setuptools import find_packages, setup


additional_files = []
for filename in glob.iglob('./pwtdata/**', recursive=True):
    if '.csv.bz' in filename:
        additional_files.append(filename.replace('./pwtdata/', ''))


setup(
    name='pwtdata',
    version='0.2.0',
    author='Tetsu Haruyama',
    author_email='haruyama@econ.kobe-u.ac.jp',
    packages=find_packages(),
    package_dir={'pwtdata': './pwtdata'},
    include_package_data=True,
    package_data={'pwtdata': additional_files},
    install_requires=['pandas'],
    url='https://github.com/spring-haru/pwtdata',
    license='LICENSE',
    description='Python package containing the Penn World Table dataset.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['data', 'Penn World Table']
)

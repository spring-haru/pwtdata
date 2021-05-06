import glob
import os
import sys
from setuptools import find_packages, setup


additional_files = []
for filename in glob.iglob('./pwtdata/**', recursive=True):
    if '.csv.bz' in filename:
        additional_files.append(filename.replace('./pwtdata/', ''))


setup(name='pwtdata',
      packages=find_packages(),
      package_dir={'pwtdata': './pwtdata'},
      version='0.2.0',
      description='Python package containing the Penn World Tables dataset.',
      author='Tetsu HARUYAMA',
      author_email='haruyama@econ.kobe-u.ac.jp',
      url='https://github.com/spring-haru/pwtdata',
      license='LICENSE.rst',
      install_requires=['pandas'],
      classifiers=['Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   ]
      )

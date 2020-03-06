from setuptools import setup, find_packages

setup(name='pwtdata',
      packages=find_packages(),
      package_dir={'pwtdata': './pwtdata'},
      version='0.1.1',
      description='Python package for downloading the Penn World Tables dataset.',
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

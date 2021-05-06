# `pwtdata`

This module contains Penn World Table 10.0. No more than that.

### How to Use
```
import pwtdata
```
* The following returns a `DataFrame` of Penn World Table 10.0.
```
pwtdata.load()
```
* There is one option: `description=True` (default is `False`) shows variable definitions
```
pwtdata.load(description=True)
```

### How to Install
```
$ pip install git+https://github.com/spring-haru/pwtdata.git
```
or
```
git clone https://github.com/spring-haru/pwtdata.git
cd pwtdata
pip install .
```

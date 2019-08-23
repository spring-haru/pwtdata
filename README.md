# `pwtdata`

The function of this module is simply to download Penn World Table 9.1 in `pandas.DataFrame`. No more than that.

**Note:**
This is based on [this `pyPWT`](https://github.com/jonduan/penn-world-tables), which is also forked from the [original `pyPWT`](https://github.com/davidrpugh/penn-world-tables).

### How to Use
```
import pwtdata
```
The following will download the dataset in a plain `DataFrame`.
```
pwtdata.load()
```
If you want `DataFrame` with `MultiIndex` (`countrycode` and `year` as row labels):
```
pwtdata.load(multi_index=True)
```

### How to Install
```
$ pip install git+https://github.com/spring-haru/pwtdata.git
```
or
```
git clone https://github.com/spring-haru/pwtdata.git
pip install .
```

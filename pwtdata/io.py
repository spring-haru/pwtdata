"""Module for downloading the Penn World Tables (PWT) data.
Module contains a set of functions that download the PWT data set.
"""
from __future__ import division
from io import BytesIO
import zipfile
import pandas as pd
import requests


def _get_dep_rates_data(base_url, version):
    """Download the depreciation rate data."""
    tmp_url = base_url + '/depreciation_rates.zip'
    tmp_buffer = requests.get(url=tmp_url)
    tmp_zip = zipfile.ZipFile(BytesIO(tmp_buffer.content))
    tmp_zip.extract('depreciation_rates.dta')


def _get_pwt_data(base_url, version):
    """Download the Penn World Tables (PWT) data."""
    tmp_url = base_url + '/pwt' + str(version) + '.dta'
    tmp_buffer = requests.get(url=tmp_url)
    with open('pwt' + str(version) + '.dta', "wb") as data:
        data.write(tmp_buffer.content)


def _download_pwt_data(base_url, version):
    """Download the Penn World Tables (PWT) data."""
    _get_dep_rates_data(base_url, version)
    _get_pwt_data(base_url, version)


def load(base_url='http://www.rug.nl/ggdc/docs/',
                  version=91, multi_index=False):
    """
    Load the Penn World Tables (PWT) data as a Pandas Panel object.

    Parameters
    ----------
        base_url : str, optional(default='http://www.rug.nl/ggdc/docs/')
            Base url to use for the download.
        version : int, optional(default=91)
            Version number for PWT data.
        multi_index : boolean, optional (default=False)
            MultiIndex with countrycode and year as row labels

    Returns
    -------
        pd.DataFrame containing the Penn World Tables (PWT) data.

    """
    try:
        pwt_raw_data = pd.read_stata('pwt' + str(version) + '.dta')
        dep_rates_raw_data = pd.read_stata('depreciation_rates.dta')

    except IOError:
        _download_pwt_data(base_url, version)
        pwt_raw_data = pd.read_stata('pwt' + str(version) + '.dta')
        dep_rates_raw_data = pd.read_stata('depreciation_rates.dta')

    # merge the data
    pwt_merged_data = pd.merge(pwt_raw_data, dep_rates_raw_data, how='outer',
                               on=['countrycode', 'year'])

    # year as int
    pwt_merged_data.year = pwt_raw_data.year.astype('int')

    # MultiIndex
    pwt_merged_data_multi = pwt_merged_data.set_index(['countrycode', 'year'])
    # return value
    if multi_index==False:
        return pwt_merged_data
    elif multi_index==True:
        return pwt_merged_data_multi

"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/stable/plugins/guides.html?#sample-data

Replace code below according to your needs.
"""

from __future__ import annotations

from ._reader import reader_function


def make_sample_data():
    # Download data from neuromorpho.org
    from urllib.request import urlretrieve

    url = "https://neuromorpho.org/dableFiles/jacobs/CNG%20version/204-2-6nj.CNG.swc"
    urlretrieve(url, "204-2-6nj.CNG.swc")
    result = reader_function("204-2-6nj.CNG.swc")
    return result

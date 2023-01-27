"""
Module to download FITS images from JSOC.
"""

from sunpy.net import Fido, attrs as a
from datetime import datetime

_all_ = ["download_fits"]


def str_to_strptime(data: str):
    return datetime.strptime(data, "%Y/%m/%d %H:%M:%S")


def download_fits(start: str, end: str, email: str):
    """
    Attributes
    ----------
    start
        Starting date
        example: "2023/01/01 00:00:00"

    end
        Ending date
        example: "2023/01/01 00:00:05"

    email
        Email registerd in JSOC, you can register here: http://jsoc.stanford.edu/ajax/exportdata.html?ds=aia.lev1_euv_12s
    """
    start = str_to_strptime(start)
    end = str_to_strptime(end)

    results = Fido.search(
        a.Time(start, end),
        a.jsoc.Series('aia.lev1_euv_12s'),
        a.jsoc.Notify(email)
    )

    print(
        f"Found {results.file_num} results. {results.file_num*2} Files will be downloaded.")
    prompt = input("Do you want to continue? [Y/n]").lower()
    if (prompt == "y"):
        Fido.fetch(results[0])

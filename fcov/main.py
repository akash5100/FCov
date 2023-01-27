#!/usr/bin/python

from downloader import download_fits
import typer
import sunpy.map
from PIL import Image
import numpy as np

app = typer.Typer()


def header_to_xml(header):
    """
    Converts image header metadata into an XML Tree that can be inserted into
    a JP2 file header.
    Parameters
    ----------
    header : `MetaDict`
        A header dictionary to convert to xml.
    Returns
    ----------
    `lxml.etree._Element`
        A fits element where each child is an xml element
        in the form <key>value</key> derived from the key/value
        pairs in the given header dictionary
    """
    # glymur uses lxml and will crash if trying to use
    # python's builtin xml.etree
    import lxml.etree as ET

    fits = ET.Element("fits")

    already_added = set()
    for key in header:
        # Some headers span multiple lines and get duplicated as keys
        # header.get will appropriately return all data, so if we see
        # a key again, we can assume it was already added to the xml tree.
        if (key in already_added):
            continue

        # Add to the set so we don't duplicate entries
        already_added.add(key)

        el = ET.SubElement(fits, key)
        data = header.get(key)
        if type(data) == bool:
            data = "1" if data else "0"
        else:
            data = str(data)

        el.text = data

    return fits


@app.command()
def download(
        start: str = typer.Option(...),
        end: str = typer.Option(...),
        email: str = typer.Option(...)):
    """
    Downloads FITS image for AIA from JSOC Instrument.
    """
    download_fits(start=start, end=end, email=email)


if __name__ == "__main__":
    # app()

    smap = sunpy.map.Map('image_lev1.fits')

    # Access the metadata
    metadata = smap.meta

    # header = header_to_xml(metadata)

    data = smap.data
    assert (data, np.ndarray)
    print(data.shape)

    # smap.save("image.jp2")

    # x = Image.open("image.jp2")
    # x.show()

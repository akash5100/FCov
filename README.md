# FCov - FITS Image Converter
FCov is a command-line tool for converting FITS images from JSOC format to JP2 format.

## Installation
To install FCov, you can use pip:

```
tbd
```

Usage
To convert a single FITS image from JSOC to JP2, use the following command:

*To be decided*
```
fcov image.fits image.jp2
```

To convert multiple FITS images at once, use the following command:

*To be decided*
```
fcov *.fits --output-dir=JP2_images/
```

## Additional Options
You can also use the following options to customize the conversion process:

- `--overwrite`: overwrite existing JP2 files with the same name
- `--quality`: set the quality level for the JP2 image (0-100)
- `--parallel`: number of parallel conversion processes to run

You can use `fcov --help` for more information about the available options.

## Dependencies
FCov requires the following dependencies to be installed:

- [sunpy](https://docs.sunpy.org/en/stable/)
- [glymur](https://glymur.readthedocs.io/)
- [typer](https://typer.tiangolo.com/)

## Support
If you have any issues or questions about FCov, please open an issue on the GitHub repository or contact the developer directly.

## Contributing
If you are interested in contributing to FCov, please see the contributing guidelines for more information.

## License
FCov is licensed under the MIT License.
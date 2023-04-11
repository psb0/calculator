%%writefile setup.py
import setuptools

setuptools.setup(
    name = 'subeen_mycalc',
    version = '0.0.1',
    description = 'nice calculator',
    author = 'psd0',
    url = 'https://github.com/psb0/calculator',
    download_url = 'https://github.com/psb0/calculator',
    packages = [ 'mycalc' ],
    classifiers = [
        'Programming Language :: Python :: 3',
    ]
)

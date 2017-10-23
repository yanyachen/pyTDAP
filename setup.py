from setuptools import setup, Extension
from Cython.Distutils import build_ext

import numpy as np

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name = 'pyTDAP',
    version = '1.0.0',

    author = 'YaChen Yan',
    author_email = 'yanyachen21@gmail.com',

    packages = ['pyTDAP'],
    url = 'https://github.com/yanyachen/pyTDAP',
    license = 'LICENSE.txt',

    description = 'Code for Time-Decaying Adaptive Prediction Algorithm.',
    long_description = read_md('README.md'),

    install_requires = [
        'cython',
        'numpy'
    ],

    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension('pyTDAP.ftrl',
                             ['pyTDAP/ftrl.pyx',
                              'pyTDAP/murmurhash/MurmurHash3.cpp'],
                             libraries = [],
                             include_dirs = [np.get_include(), '.'],
                             extra_compile_args = ['-O3']),
                   Extension('pyTDAP.tdap',
                             ['pyTDAP/tdap.pyx',
                              'pyTDAP/murmurhash/MurmurHash3.cpp'],
                             libraries = [],
                             include_dirs = [np.get_include(), '.'],
                             extra_compile_args = ['-O3']),
                   Extension('pyTDAP.util',
                             ['pyTDAP/util.pyx', 'pyTDAP/util.pxd'],
                             libraries = [],
                             include_dirs = [np.get_include(), '.'],
                             extra_compile_args = ['-O3'])],
)

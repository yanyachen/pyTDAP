# pyTDAP
pyTDAP is a Python package for lightweight Time-Decaying Adaptive Prediction Algorithm.
Original paper is available at [here](https://goo.gl/jf2Puh)

It is distributed under the version 3 of the GNU General Public License. It uses the sparse input format that handles large sparse data efficiently.  Core code is optimized for speed by using Cython.


# Motivation
This package implements TDAP algorithm for comparing with FTRL in fast-changing nature.
The FTRL code is adopted from Jeong-Yoon Lee's package [Kaggler](https://github.com/jeongyoonlee/Kaggler)


# Algorithms
Currently algorithms available are as follows:
* Time-Decaying Adaptive Prediction (TDAP)
* Follow-the-Regularized-Leader (FTRL)


# Dependencies
Python packages required are listed in `requirements.txt`
* cython
* numpy


# Installation
## From source code
If you want to install it from source code:
```
python setup.py build_ext --inplace
sudo python setup.py install
```

# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True
from __future__ import division

import logging
import numpy as np

cimport cython
from libc.math cimport exp, log
cimport numpy as np


np.import_array()


cdef double sigm(double x):
    """Bounded sigmoid function."""
    return 1 / (1 + exp(-fmax(fmin(x, 20.0), -20.0)))

#!/usr/bin/env python3

# import sys
# print(sys.path)

try:
    import numpy as np
    print("NumPy is installed. Version:", np.__version__)
except ImportError:
    print("NumPy is not installed. Please install it using 'pip install numpy'.")


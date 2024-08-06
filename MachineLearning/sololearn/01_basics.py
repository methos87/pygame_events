#!usr/bin/env python

import numpy as np
import matplotlib
import pandas
import math

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean is {}".format(np.mean(data)))
print("median is {}".format(np.median(data)))
print("variance is {}".format(np.var(data)))
print("standard deviation is {}".format(np.std(data)))
print("25th percentile is {}".format(np.percentile(data, 25)))

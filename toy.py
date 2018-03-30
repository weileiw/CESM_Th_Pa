import numpy as np
import matplotlib.pyplot as plt
import scipy.io as io
import sys
from geoplots import geoplot
import os.path
from scipy.io import loadmat
from scipy.io import whosmat
from scipy.optimize import curve_fit


def func(x, a, b):
    return a * x + b


file1 = 'run003_90x180x60.mat'
run001 = loadmat(file1)
Pa231_cesm = run001['Pa231']
Th230_cesm = run001['Th230']

data_path = os.path.expanduser('~/Dropbox/MOCM/DATA')
msk_name = os.path.join(data_path, 'M3d90x180x24v2.mat')
msk = loadmat(msk_name, squeeze_me=True, struct_as_record=False)
ATL = msk['MSKS'].ATL
ATL = ATL[:, :, 0:1]

R = (Pa231_cesm / Th230_cesm) * ATL
ATL_R = np.nanmean(R, axis=1).squeeze()
print(ATL_R.shape)

import datetime
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def hw_process(y, outpush=1, damping_slope=0.9, **kwargs):
    md = ExponentialSmoothing(endog=y, **kwargs).fit(damping_slope=damping_slope)
    n_y = len(y)
    fcst= md.predict(start=0, end=n_y + outpush -1)
    fcst_histr, fcst_future = fcst[:n_y], fcst[n_y:]
    return fcst_histr, fcst_future


def get_spectral_info(y):
    N = len(y)
    ffy = np.fft.fft(y)
    ffy_abs = np.abs(ffy)[1:int(N / 2)]
    freq = np.arange(N)[1:int(N / 2)]
    return ffy_abs, freq


def wmape(y_fcst, y_true):
    return np.abs(y_fcst - y_true).sum() / y_true.sum()
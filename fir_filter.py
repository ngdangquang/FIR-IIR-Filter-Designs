import numpy as np
from scipy.signal import firwin

# Design FIR filter using windowing method
def design_fir_with_window(N, cutoff, fs, window_type='hann'):
    """
    Design an FIR filter using the windowing method.
    
    Parameters:
    N : int - Filter order (number of taps)
    cutoff : float - Cutoff frequency (Hz)
    fs : float - Sampling frequency (Hz)
    window_type : str - Window function (default 'hann')
    
    Returns:
    fir_coeff : numpy array - Filter coefficients
    """
    return firwin(N, cutoff / (0.5 * fs), window=window_type)

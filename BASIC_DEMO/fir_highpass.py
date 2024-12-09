import numpy as np
from scipy.signal import kaiserord, lfilter, firwin, freqz, firwin2
import matplotlib.pyplot as plt

# Nyquist rate.
nyq_rate = 48000 / 2

# Width of the roll-off region.
width = 500 / nyq_rate

# Attenuation in the stop band.
ripple_db = 12.0

num_of_taps, beta = kaiserord(ripple_db, width)
if num_of_taps % 2 == 0:
    num_of_taps = num_of_taps + 1

# Cut-off frequency.
cutoff_hz = 5000.0

# Estimate the filter coefficients.
taps = firwin(num_of_taps, cutoff_hz/nyq_rate, window=('kaiser', beta), pass_zero=False)

w, h = freqz(taps, worN=4000)

plt.plot((w/np.pi)*nyq_rate, 20*np.log10(np.abs(h)), linewidth=2)

plt.axvline(cutoff_hz + width*nyq_rate, linestyle='--', linewidth=1, color='g')
plt.axvline(cutoff_hz - width*nyq_rate, linestyle='--', linewidth=1, color='g')
plt.axhline(-ripple_db, linestyle='--', linewidth=1, color='c')
delta = 10**(-ripple_db/20)
plt.axhline(20*np.log10(1 + delta), linestyle='--', linewidth=1, color='r')
plt.axhline(20*np.log10(1 - delta), linestyle='--', linewidth=1, color='r')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Frequency Response')
plt.ylim(-40, 5)
plt.grid(True)
plt.show()
import numpy as np
from scipy.signal import kaiserord, lfilter, firwin, freqz
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

# Bandpass filter cutoff frequencies.
low_cutoff_hz = 3000.0  # Lower cutoff frequency in Hz
high_cutoff_hz = 7000.0  # Upper cutoff frequency in Hz

# Estimate the filter coefficients for a bandpass filter.
taps = firwin(num_of_taps, [low_cutoff_hz/nyq_rate, high_cutoff_hz/nyq_rate], window=('kaiser', beta), pass_zero=False)

# Frequency response.
w, h = freqz(taps, worN=4000)

# Plot the frequency response.
plt.plot((w/np.pi)*nyq_rate, 20*np.log10(np.abs(h)), linewidth=2)

# Highlight the bandpass filter passband and ripple limits.
plt.axvline(low_cutoff_hz, linestyle='--', linewidth=1, color='g')
plt.axvline(high_cutoff_hz, linestyle='--', linewidth=1, color='g')
plt.axhline(-ripple_db, linestyle='--', linewidth=1, color='c')
delta = 10**(-ripple_db/20)
plt.axhline(20*np.log10(1 + delta), linestyle='--', linewidth=1, color='r')
plt.axhline(20*np.log10(1 - delta), linestyle='--', linewidth=1, color='r')

# Labels and title.
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Bandpass Filter Frequency Response')
plt.ylim(-40, 5)
plt.grid(True)
plt.show()
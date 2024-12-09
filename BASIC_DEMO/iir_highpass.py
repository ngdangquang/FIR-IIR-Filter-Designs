import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

# Set parameters
fs = 48000  # Sampling frequency (Hz)
nyq_rate = fs / 2

# Filter parameters
cutoff_hz = 5000.0       # Cutoff frequency (Hz)
order = 4                 # Filter order

# Design IIR Highpass filter (Butterworth)
b, a = butter(order, cutoff_hz / nyq_rate, btype='high', analog=False)

# Compute frequency response
w, h = freqz(b, a, worN=8000)

# Plot frequency response
plt.figure(figsize=(10, 6))
plt.plot((w / np.pi) * nyq_rate, 20 * np.log10(np.abs(h)), linewidth=2, label='IIR Highpass')
plt.axvline(cutoff_hz, linestyle='--', linewidth=1, color='g', label='Cutoff Frequency')
plt.axhline(-40, linestyle='--', linewidth=1, color='c', label='Stopband Attenuation')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('IIR Highpass Filter Frequency Response (Butterworth)')
plt.ylim(-60, 5)
plt.grid(True)
plt.legend()
plt.show()

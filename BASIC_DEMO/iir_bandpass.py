import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

# Set parameters
fs = 48000  # Sampling frequency (Hz)
nyq_rate = fs / 2

# Filter parameters
low_cutoff_hz = 5000.0    # Low cutoff frequency (Hz)
high_cutoff_hz = 10000.0  # High cutoff frequency (Hz)
order = 4                 # Filter order

# Design IIR Bandpass Filter (Butterworth)
b, a = butter(order, [low_cutoff_hz / nyq_rate, high_cutoff_hz / nyq_rate], btype='band')

# Compute frequency response
w, h = freqz(b, a, worN=8000)

# Plot frequency response
plt.figure(figsize=(10, 6))
plt.plot((w / np.pi) * nyq_rate, 20 * np.log10(np.abs(h)), linewidth=2, label='IIR Bandpass')
plt.axvline(low_cutoff_hz, linestyle='--', linewidth=1, color='g', label='Low Cutoff Frequency')
plt.axvline(high_cutoff_hz, linestyle='--', linewidth=1, color='g', label='High Cutoff Frequency')
plt.axhline(-40, linestyle='--', linewidth=1, color='c', label='Stopband Attenuation')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('IIR Bandpass Filter Frequency Response (Butterworth)')
plt.ylim(-60, 5)
plt.grid(True)
plt.legend()
plt.show()

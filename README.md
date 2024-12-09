# Digital Filter Designs

This project demonstrates the design and implementation of both FIR (Finite Impulse Response) and IIR (Infinite Impulse Response) filters in Python. The filters are designed using well-known techniques and are applied to noisy signals to observe their performance in filtering.

## Files:
- **theory.md**: Contains the theory of FIR and IIR filters, their advantages, disadvantages, and the methods used for their design.
- **fir_filter.py**: Contains the implementation for designing FIR filters using the windowing method, and how to apply them.
- **iir_filter.py**: Contains the implementation for designing IIR filters using the Chebyshev method, a common approach for analog-to-digital conversion.
- **filter_testing.py**: Main script that demonstrates the use of both FIR and IIR filters on noisy signals. It plots the noisy signal, the FIR filtered signal, and the IIR filtered signal for comparison.
- **signals.py**: Utility script for generating noisy signals, which consist of sine waves mixed with Gaussian noise. The noisy signal is used to test the performance of the filters.

- **iir_lowpass.py**: Demonstrates the design and implementation of an IIR low-pass filter using the Butterworth method.
- **iir_highpass.py**: Demonstrates the design and implementation of an IIR high-pass filter using the Butterworth method.
- **iir_bandpass.py:**: Demonstrates the design and implementation of an IIR bandpass filter using the Butterworth method.
- **fir_bandstop.py:**: Demonstrates the design and implementation of an FIR bandstop filter using the Kaiser windowing method.
- **fir_lowpass.py:**: Demonstrates the design and implementation of an FIR low-pass filter using the Kaiser windowing method.
- **fir_highpass.py:**: Demonstrates the design and implementation of an FIR high-pass filter using the Kaiser windowing method.
- **fir_bandpass.py**: Demonstrates the design and implementation of an FIR bandpass filter using the Kaiser windowing method.
## Requirements:
Make sure to install the following dependencies to run this project:
- `numpy`: For numerical operations
- `scipy`: For signal processing functions and filter design
- `matplotlib`: For plotting graphs and visualizing results

To install the dependencies, run:
    pip install numpy scipy matplotlib


## How to Run:
1. Make sure all the `.py` files are in the same directory.
2. Run the script `filter_testing.py` to observe how the filters perform on a noisy signal or files in folder `BASIC_DEMO` to observe the basic theory of FIR and IIR filters and how they are designed.
3. Check the plots generated to compare the original noisy signal with the filtered outputs.

## Theory and Design:
The theory behind the filters and their design can be found in the `theory.md` file. In summary, FIR filters are typically used for their stability, while IIR filters are more computationally efficient and can achieve the same frequency response with fewer coefficients.

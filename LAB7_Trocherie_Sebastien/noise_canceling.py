# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:18:46 2022

@author: troch
"""

import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
import csv 

path="wave.csv"
first = 0
file= open(path, newline='')
reader = csv.reader(file)
header = next(reader)   #first line is the header 

step=[]
wave1=[]
wave2=[]
wave3=[]
signal=[]
sum1=[]
sum2=[]
sum3=[]
for row in reader:
    temp_step = int(row[0])
    step.append(temp_step)
    temp_wave1=int(row[1])
    wave1.append(temp_wave1)
    temp_wave2=int(row[2])
    wave2.append(temp_wave2)
    temp_wave3=int(row[3])
    wave3.append(temp_wave3)
    signal.append(temp_wave1 + temp_wave2 + temp_wave3)
    sum1.append(temp_wave1 + temp_wave2)
    sum2.append(temp_wave2 + temp_wave3)
    sum3.append(temp_wave1 + temp_wave3)


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
fig.suptitle('3 waves + total wave')
ax1.plot(step, wave1)
ax2.plot(step, wave2)
ax3.plot(step, wave3)
ax4.plot(step, signal)  

ax1.set_xlim(0,2000)
ax2.set_xlim(0,2000)
ax3.set_xlim(0,2000)
ax4.set_xlim(0,2000)

sig_fft = fftpack.fft(signal)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(len(signal),d=1)

# Plot the FFT power
plt.figure(figsize=(10, 20))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')
plt.xlim(-0.05,0.05)
plt.show()

pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]
print(peak_freq)

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

sig_fft1 = fftpack.fft(filtered_sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft1)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(len(filtered_sig), d=1)

plt.figure(figsize=(10, 20))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')
plt.xlim(-0.05,0.05)
plt.show()

plt.figure(figsize=(60,10))
plt.plot(step, signal, label='Original signal')
plt.plot(step, filtered_sig, linewidth=3, label='Filtered signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.legend(loc='best')
plt.xlim(0,2000)
plt.show()


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
fig.suptitle('3 waves + total wave')
ax1.plot(step, sum1)
ax2.plot(step, sum2)
ax3.plot(step, sum3)
ax4.plot(step, filtered_sig)  

ax1.set_xlim(0,2000)
ax2.set_xlim(0,2000)
ax3.set_xlim(0,2000)
ax4.set_xlim(0,2000)


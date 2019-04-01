import numpy as np
import scipy.signal as sp

class Smoothing:

    def __init__(self, intensity):
        self.intensity = intensity



    @staticmethod
    def SavitzkyGolay(intensity, polyNo, window=None ):
        if window==None:
            window = int(np.round(len(intensity)/4))
            print(window)
        if window%2 == 0:
            window = int(window) +1
        if polyNo >= window:
            polyNo = window -1

        SavSmoothed = sp.savgol_filter(intensity,window, polyNo)
        return SavSmoothed

    @staticmethod
    def SmoothFFT(intensity, cutoff):
        fft = np.fft.fft(intensity)
        fft[int(round(len(fft)*cutoff)):len(fft)] = 0
        FftSsmoothed = np.real(np.fft.ifft(fft))
        return FftSsmoothed

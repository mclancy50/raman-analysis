import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Source import Normalisation, Smoothing, RamanSpectrum
from scipy.interpolate import interp1d

class BackgroundFitting:

    def __init__(self, intensity, type = None):
        self.intensity = intensity
        if type==None:
            type = 'default'

    @staticmethod
    def backgroundSubtraction(x,y, plot=False):
        peaks = sp.signal.find_peaks(y)
        smoothed = Smoothing.Smoothing.SavitzkyGolay(y,2,window = None)
        #fitted = smoothed - np.abs(smoothed[1]-y[1])
        fitted = BackgroundFitting.fitPolynomial(x,smoothed,11)

        bkgdSub= np.subtract(y,fitted)
        #if np.min(bkgdSub)<0:
         #   bkgdSub = bkgdSub - np.min(bkgdSub)
        if plot:
            plt.figure()
            plt.subplot(2, 1, 1)
            RamanSpectrum.RamanSpectrum.plotSpectrum(x,y, title='Original Spectrum')
            #RamanSpectrum.RamanSpectrum.plotSpectrum(x,smoothed, title='Smoothed Spectrum')
            RamanSpectrum.RamanSpectrum.plotSpectrum(x,fitted, title='Background Fit')
            plt.legend()
            plt.subplot(2, 1, 2)
            RamanSpectrum.RamanSpectrum.plotSpectrum(x,bkgdSub, title='Background Subtracted Data')
            plt.legend()
        return bkgdSub

    @staticmethod
    def fitPolynomial(x,y, degree=4, plot=False):
        fit = np.polyfit(x,y,degree)
        fittedIntensity = np.polyval(fit,x)
        if plot:
            plt.figure()
            RamanSpectrum.RamanSpectrum.plotSpectrum(y, 'Original Data')
            RamanSpectrum.RamanSpectrum.plotSpectrum(fittedIntensity, 'Polynomial fit')
            plt.legend()
        return fittedIntensity

    @staticmethod
    def calculateGradient(x,y,plot=False):
        grad = np.gradient(y)
        RamanSpectrum.RamanSpectrum.plotSpectrum(x,grad,'Gradient')




import numpy
import datetime, time
import matplotlib.pyplot as plt
import sklearn.preprocessing as sk
import scipy.signal as sp
from Source import Normalisation, Smoothing, BackgroundFitting


class RamanSpectrum:
    def __init__(self, wavenumber, intensity, filename):
        self.wavenumber = wavenumber
        self.OriginalSpectrum = intensity
        self.intensity = intensity
        self.filename = filename
        self.processingReport = []

    def plot(self):
        self.plotSpectrum(self.wavenumber,self.intensity,self.filename)

    @staticmethod
    def plotSpectrum(x,y,title):
        plt.plot(x,y, label=title)
        plt.title(title, loc='center')
        plt.xlabel('Wavenumber (cm-1)')
        plt.ylabel('Intensity (AU)')
        plt.show()

    def setErrorBars(self, errorArray):
        self.error = errorArray

    def smoothfft(self, cutoff, plot=False):
        self.preFilter = self.intensity
        self.intensity = Smoothing.Smoothing.SmoothFFT(self.intensity,cutoff)
        if plot:
            plt.figure()
            self.plotSpectrum(self.wavenumber,self.preFilter, title='Data Prior to Filtering')
            self.plotSpectrum(self.wavenumber,self.intensity,  title='Fft Smoothed Data')
            plt.legend()
        self.updateProcessReport(("Data Smoothed using fft removing highest " + str(100-(cutoff*100)) + " % of frequencies"))
        return self.intensity

    def smoothSavGol(self, polyNo, window = None, plot = False):
        self.preFilter = self.intensity
        self.intensity = Smoothing.Smoothing.SavitzkyGolay(self.intensity, polyNo, window)
        if plot:
            plt.figure()
            RamanSpectrum.plotSpectrum(self.wavenumber,self.preFilter, title='Data Prior to Filtering')
            RamanSpectrum.plotSpectrum(self.wavenumber,self.intensity, title='SavGol Smoothed Data')
            plt.legend()
        self.updateProcessReport("Savitsky-Golay Smoothing applied. Window size: " + str(window) + " Polynomial Order: " + str(polyNo))
        return self.intensity

    def normalise(self,min,max):
        self.preFilter = self.intensity
        self.intensity = Normalisation.Normalisation.minMaxNorm(self.intensity,min,max)
        self.updateProcessReport(("Data Normalised between " + str(min) + " and " + str(max)) )
        return self.intensity

    def backgroundSubtraction(self,window=None, plot=False):
        self.preFilter = self.intensity
        self.intensity = BackgroundFitting.BackgroundFitting.backgroundSubtraction(self.wavenumber,self.intensity,plot)
        self.updateProcessReport("Background subtracted out")
        return self.intensity

    def updateProcessReport(self,update):
        currentTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.processingReport.append(currentTime + update)

    def undoLastChange(self):
        self.intensity = self.preFilter
        self.updateProcessReport(" Preceeding change undone")





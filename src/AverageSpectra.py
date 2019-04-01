import numpy as np
from Source import RamanSpectrum
from mpltools import special
import matplotlib.pyplot

class AverageSpectra:

    def __init__(self,listOfSpectra):
        self.listOfSpectra = listOfSpectra

    def averageListedSpectra(self, plot=False):
        self.dataMatrix = np.empty(shape=(len(self.listOfSpectra),len(self.listOfSpectra[1].wavenumber)))
        for i in range(0,len(self.listOfSpectra)):
            self.dataMatrix[i,]=self.listOfSpectra[i].intensity
        self.avgSpec = RamanSpectrum.RamanSpectrum(self.listOfSpectra[1].wavenumber,np.mean(self.dataMatrix,axis=0),'Average Spectrum')
        self.calculateStndDeviation()
        if plot:
            self.plotAverage()
        self.avgSpec.setErrorBars(self.stdDev)
        return self.avgSpec

    def calculateStndDeviation(self):
        self.stdDev = np.std(self.dataMatrix, axis=0)
        print(len(self.stdDev))
        return self.stdDev

    def plotAverage(self):

        matplotlib.pyplot.title(self.avgSpec.filename, loc='center')
        matplotlib.pyplot.xlabel('Wavenumber (cm-1)')
        matplotlib.pyplot.ylabel('Intensity (AU)')
        special.errorfill(self.avgSpec.wavenumber, self.avgSpec.intensity, self.stdDev ,color='r')
        matplotlib.pyplot.show()


"""
Create 3D waterfall plot from a list of 'RamanSpectrum' objects.
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colors as mcolors
import numpy as np

class WaterfallPlot():

    def __init__(self, SpectraList, title=None):
        self.title=title
        self.SpectraList = SpectraList
        self.plotWaterfall()

    def cc(arg):
        return mcolors.to_rgba(arg, alpha=0.6)

    def plotWaterfall(self):
        z_values = np.arange(0,len(self.SpectraList),1)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        verts = []
        cmap = matplotlib.cm.get_cmap('Spectral')
        colour_ident = np.arange(0,1,1/len(z_values))
        colours=[]
        for i in range(0, len(self.SpectraList)):
            self.SpectraList[i].smoothSavGol(3, window=31)
            self.SpectraList[i].normalise(0,1)
            verts.append(list(zip(self.SpectraList[i].wavenumber,self.SpectraList[i].intensity)))
            colours.append((cmap(colour_ident[i])))

        poly = PolyCollection(verts,facecolors = colours, edgecolors='k')
        poly.set_alpha(0.7)

        ax.add_collection3d(poly, zs=z_values, zdir='y')
        ax.set_title(self.title)
        ax.set_xlabel('Wavenumber (cm-1)')
        ax.set_xlim3d(np.min(self.SpectraList[i].wavenumber),np.max(self.SpectraList[i].wavenumber))
        ax.set_ylabel('Timepoint No.')
        ax.set_ylim3d(np.min(z_values), np.max(z_values))
        ax.set_zlabel('Intensity')
        ax.set_zlim3d(np.min(self.SpectraList[i].intensity),np.max(self.SpectraList[i].intensity))
        plt.show()
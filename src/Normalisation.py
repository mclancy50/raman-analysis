import numpy as np

class Normalisation:
    def __init__(self,dataarray):
        self.dataarray = dataarray

    @staticmethod
    def minMaxNorm(dataarray,rangemin,rangemax):
        if np.min(dataarray) < 0:
           dataarray = dataarray-np.min(dataarray)
        dataNorm = ((rangemax-rangemin)*((dataarray-np.min(dataarray))/(np.max(dataarray)-np.min(dataarray)))) + rangemin
        return dataNorm
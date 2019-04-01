import numpy as np
import os
from Source.RamanSpectrum import RamanSpectrum


class ImportRamanData:

    def __init__(self, directory_list, sample_names):
        self.sample_names = sample_names
        self.directory_list = directory_list
        self.txt_file_list = np.array([])
        self.index = np.array([])
        self.target_name = np.array([])
        self.raman_data = []
        print(self.directory_list)

        self.collateLists()
        self.importFilesToRamanSpectra()

    def collateLists(self):

        for i in range(0, len(self.directory_list)):
            try:
                files = os.listdir(self.directory_list[i])
                self.referencefilenames = []
                for is_txt in files:
                    if is_txt.endswith(".txt"):
                        self.index = np.append(self.index, i)
                        file_name_to_add = self.directory_list[i] + "\\" + is_txt
                        self.referencefilenames.append(is_txt)
                        self.txt_file_list = np.append(self.txt_file_list, file_name_to_add)

                        if len(self.sample_names) > 0:
                            self.target_name = np.append(self.target_name, self.sample_names[i])
                print("Directory ", i, ":", len(self.txt_file_list), " text files imported for sample type: ", self.sample_names[i])
                print(self.txt_file_list)
            except NotADirectoryError:
                print("Directory", self.directory_list[i], " is invalid")

    def importFilesToRamanSpectra(self):
        for i in range(0, len(self.txt_file_list)):
            print("Attempting to open: ", [self.txt_file_list[i]])
            current_file = self.txt_file_list[i]
            wavenumber, intensity = np.loadtxt(fname=current_file, dtype=([('x', 'd'), ('y', 'd')]), unpack=True,
                                               skiprows=1)
            self.raman_data.append(RamanSpectrum(np.transpose(wavenumber),np.transpose(intensity),self.referencefilenames[i]))

        return self.raman_data




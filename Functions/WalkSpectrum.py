from FilterSpectrum import *
import numpy as np
import gc
def WalkSpectrum(DataSet,MSLevel=1,min_RT=0,max_RT=300,minInt=1e5,min_mz=50,max_mz=1000):
    AllSpectrum=np.zeros((2,3))
    for spectra in DataSet:
        RT=spectra.getRT()
        ML=spectra.getMSLevel()
        AllSpectrum=FilterSpectrum(AllSpectrum=AllSpectrum,spectra=spectra,ML=ML,RT=RT,min_RT=min_RT,max_RT=max_RT,minInt=minInt,min_mz=min_mz,max_mz=max_mz,MSLevel=MSLevel)
    SortSpectrumLoc=np.argsort(AllSpectrum[:,0])        
    AllSpectrum=AllSpectrum[SortSpectrumLoc,:]
    del SortSpectrumLoc
    del RT
    del ML
    gc.collect()
    return AllSpectrum

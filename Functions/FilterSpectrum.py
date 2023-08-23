import numpy as np
def FilterSpectrum(AllSpectrum,spectra,RT,ML,min_RT=0,max_RT=100,minInt=1e5,min_mz=50,max_mz=1000,MSLevel=1):
    if (ML==MSLevel)&(RT<max_RT)&(RT>min_RT):
        RawSpectra_NoRT=np.array(spectra.get_peaks()).T
        FilterLoc=np.where((RawSpectra_NoRT[:,1]>minInt)&(RawSpectra_NoRT[:,0]>min_mz)&(RawSpectra_NoRT[:,0]<max_mz))[0]
        Spectra_NoRT=RawSpectra_NoRT[FilterLoc,:]
        Spectra=np.c_[Spectra_NoRT,RT*np.ones(np.shape(Spectra_NoRT)[0])]        
        if np.shape(AllSpectrum)[0]>2:
            AllSpectrum=np.r_[AllSpectrum,Spectra.copy()]
        else:
            AllSpectrum=Spectra.copy()
        del RawSpectra_NoRT
        del FilterLoc
        del Spectra_NoRT
        del Spectra
    return AllSpectrum

import numpy as np
def SampleSpectrum(AllSpectrum,fraction=20):
    PopulationSize=np.shape(AllSpectrum)[0]
    SampleSize=int(PopulationSize*fraction/100)
    SampleLoc=np.linspace(0,PopulationSize-1,SampleSize,dtype='int')
    SampleSpectrum=AllSpectrum[SampleLoc,:].copy()
    del PopulationSize
    del SampleSize
    del SampleLoc
    return SampleSpectrum

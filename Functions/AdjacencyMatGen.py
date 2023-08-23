import numpy as np
import gc
#Replacing the clustring strategy with the minimum distance
def AdjacencyMatGen(Spectrum,mz_Tol=5e-5,RT_Tol=5):
    AdjacencyMatrix=[]
    for signal in Spectrum:
        mz=signal[0]
        RT=signal[2]
        mz_max=mz+mz_Tol
        mz_min=mz-mz_Tol
        RT_max=RT+RT_Tol
        RT_min=RT-RT_Tol
        NeighborsLoc=np.where((Spectrum[:,0]>mz_min)&(Spectrum[:,0]<mz_max)&(Spectrum[:,2]<RT_max)&(Spectrum[:,2]>RT_min))[0]
        AdjacencyMatrix.append(NeighborsLoc)
    del mz
    del RT
    del mz_max
    del mz_min
    del RT_max
    del RT_min
    del NeighborsLoc
    gc.collect()
    return AdjacencyMatrix

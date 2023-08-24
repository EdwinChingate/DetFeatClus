import numpy as np
import gc
def DistanceKernel(signal,Kernel):
    D_RT=np.abs(signal[2]-Kernel[:,0])
    D_mz=np.abs(signal[0]-Kernel[:,2])
    DistanceVec=D_RT/signal[2]+D_mz/signal[0]
    DistanceMat=np.c_[D_RT,D_mz,DistanceVec,np.arange(len(Kernel[:,0]))]
    del D_RT
    del D_mz
    del DistanceVec
    gc.collect()
    return DistanceMat

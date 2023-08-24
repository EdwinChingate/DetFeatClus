from EmptyModules import *
from DistanceKernel import *
from Pre_SelectCentroid import *
from SelectCentroid import *
import gc 
def ModulesK_Nearst(Signals,Kernel,SafetyFactor=4):
    signalID=0
    Modules=EmptyModules(len(Kernel[:,0]))
    for signal in Signals:
        DistanceMat=DistanceKernel(signal,Kernel)
        pre_Centroid=Pre_SelectCentroid(DistanceMat=DistanceMat,Kernel=Kernel,SafetyFactor=SafetyFactor)
        if len(pre_Centroid)>0:
            ID=int(SelectCentroid(DistanceMat[pre_Centroid,:]))
        else:
            ID=-1
        Modules[ID].append(signalID)
        signalID+=1
        del DistanceMat
        del pre_Centroid
        gc.collect()
    return Modules

import numpy as np
from ModulesDetMax import *
import gc
def MaxIntCentroids(Spectrum,AdjacencyMatrix,KernelIDs=[],features=0,FeaturesNumber=500,MinSignals=3,MinIntKernel=3e4,MaxDeep=3):        
    MaxInt=MinIntKernel*1.5
    VisitVector=np.zeros(len(AdjacencyMatrix))
    while features<FeaturesNumber and MaxInt>MinIntKernel:
        MaxInt=np.max(Spectrum[:,1])
        Loc=np.where(Spectrum[:,1]==MaxInt)[0][0]
        Module=ModulesDetMax(MaxID=Loc,AdjacencyMatrix=AdjacencyMatrix,VisitVector=VisitVector,Module=[Loc],MaxDeep=MaxDeep)       
        del Loc
        CleanModule=list(set(Module))
        if len(CleanModule)>MinSignals:
            KernelIDs.append(CleanModule)
            features+=1
        Spectrum[Module,1]=0
        del Module
        gc.collect()
    del MaxInt     
    gc.collect()
    if features==FeaturesNumber:
        print('There are more features')
    return KernelIDs

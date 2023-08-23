import numpy as np
import gc
def ModulesDetMax(MaxID,AdjacencyMatrix,VisitVector,Module=[],deep=0,MaxDeep=3):
#This is function also check for neightboors, but not more than 'MaxDeep', which is not a problem, as this function is just a first step in the clustering    
    CurrentModule=AdjacencyMatrix[MaxID]
    VisitVector[MaxID]=VisitVector[MaxID]+1
    if len(CurrentModule)>1:    
        VisitVector[CurrentModule]=VisitVector[CurrentModule]+1
        for KernelID in CurrentModule:
            Module.append(KernelID)
            if deep<MaxDeep and VisitVector[KernelID]<2:                
                Module=ModulesDetMax(MaxID=KernelID,AdjacencyMatrix=AdjacencyMatrix,VisitVector=VisitVector,deep=deep+1,MaxDeep=MaxDeep,Module=Module)        
    del CurrentModule
    del deep
    gc.collect()
    return Module

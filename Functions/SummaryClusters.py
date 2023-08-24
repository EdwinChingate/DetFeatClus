from SignalsStats import *
import pandas as pd
import numpy as np
def SummaryClusters(Signals,Modules,alpha=0.01,ReturnDF=True,columns=["AverageRT","StdRT","AverageMZ","StdMZ","l","ConfidenceIntervalDa","ConfidenceInterval","SumInt"]):    
    Summary=[]
    for mod in Modules:
        signalsStats=SignalsStats(Signals[mod,:],alpha=alpha)
        Summary.append(signalsStats)
    SummaryArray=np.array(Summary)
    SummaryArrSort=np.argsort(SummaryArray[:,2])
    if ReturnDF:
        SummaryDF=pd.DataFrame(SummaryArray[SummaryArrSort,:])    
        return SummaryDF
    else:
        return SummaryArray[SummaryArrSort,:]

from scipy.stats import t
import numpy as np
from ChromatogramShapeTest import *
def SignalsStats(Signals,alpha=0.01): #Isotopomer refers to either the most abundant isotopomer, or the one with 18O
    SumIntens=sum(Signals[:,1])
    RelativeInt=Signals[:,1]/SumIntens
    AverageMZ=sum(Signals[:,0]*RelativeInt)
    AverageRT=sum(Signals[:,2]*RelativeInt)
    l=len(Signals[:,1])    
    VarianMZ=sum(RelativeInt*(Signals[:,0]-AverageMZ)**2)*l/(l-1)  
    StdMZ=np.sqrt(VarianMZ)
    VarianRT=sum(RelativeInt*(Signals[:,2]-AverageRT)**2)*l/(l-1)    
    StdRT=np.sqrt(VarianRT)    
    tref=t.interval(1-alpha, l-1)[1]
    ConfidenceIntervalDa=tref*StdMZ/np.sqrt(l)
    ConfidenceInterval=ConfidenceIntervalDa/AverageMZ*1e6
    [m,r2]=ChromatogramShapeTest(Signals)
    signalsStats=[AverageRT,StdRT,AverageMZ,StdMZ,l,ConfidenceIntervalDa,ConfidenceInterval,SumIntens,m,r2]    
    return signalsStats

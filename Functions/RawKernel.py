from SignalsStats import *
def RawKernel(Signals,KernelIDs,alpha=0.01,minr2=0.5):    
    Kernel=[]
    for cent in KernelIDs:
        signalsStats=SignalsStats(Signals[cent,:],alpha=alpha)
        if signalsStats[8]<0 and signalsStats[9]>minr2:
            Kernel.append(signalsStats[:8])        
    KernelArray=np.array(Kernel)
    return KernelArray

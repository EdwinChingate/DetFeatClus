import numpy as np
from scipy import stats
def ChromatogramShapeTest(Signals):
    MaxInt=np.max(Signals[:,1])
    MaxIntLoc=np.where(Signals[:,1]==MaxInt)[0]
    MaxRT=Signals[MaxIntLoc,2]
    RTvec2=(Signals[:,2]-MaxRT)**2
    Reg=stats.linregress(x=RTvec2, y=Signals[:,1], alternative='two-sided')
    return [Reg[0],-Reg[2]]

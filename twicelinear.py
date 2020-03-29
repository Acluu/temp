import numpy as np
def dbl_linear(n):
    db=np.array([1])
    tpt=np.array([1])
    for i in range(10):
        t1=tpt*2+1
        t2=tpt*3+1
        tpt=np.unique(np.append(t1,t2))
        db=np.unique(np.append(db,tpt))
    return db[n]

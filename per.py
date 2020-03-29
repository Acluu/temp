def persistence(n):
    r=1
    while(n>10):
        for t in [int (i) for i in list(str(n))]:
            
            r*=t
        n=r
                
        if (n<10):
            return n
        r=1
    return r
    

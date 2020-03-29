def dig_pow(n, p):
    import math
    digits=[]
    nn=n
    s=0
    while(n/10!=0):
        digits.append(n%10)
        n=int(n/10)
    print(digits)
    for d in digits[::-1]:
        s=s+math.pow(d,p)
        p+=1
    if s%nn==0:
        return s/nn
    return -1

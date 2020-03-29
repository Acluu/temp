def find_nb(m):
    for i in range(1,500000):
        m-=i**3
        if m<0:
            return -1;
        if m==0:
            return i
    return -1

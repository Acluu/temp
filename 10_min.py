def is_valid_walk(walk):
    if (len(walk)<=1)|(len(walk)>10):
        return False
    di_to_num={'n':0+1j,'s':0-1j,'w':-1,'e':1}
    pos=0
    for di in walk:
        pos=pos+di_to_num[di]
        print(pos)
    if pos==0:
        return True
    else:
        return False
    pass

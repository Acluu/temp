def en(c):
    alph=[chr(i) for i in range(97,123)]
    Alph=[chr(i) for i in range(65,91)]
    if ((c in alph)&(ord(c)<110)):
        return chr(ord(c)+13)
    elif ((c in Alph)&(ord(c)<78)):
        return chr(ord(c)+13)
    elif c in alph:
        return chr(ord(c)-13)
    else:
        return chr(ord(c)-13)
    return None
        
def rot13(message):
    origin=list(message)
    out=""
    for ch in origin:
        if ((97<=ord(ch)<=122)|(65<=ord(ch)<=90)):
            out+=en(ch)
        else:
            out+=ch
    print(out)

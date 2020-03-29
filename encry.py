def decrypt(encrypted_text, n):
    if ((n<=0)|(len(encrypted_text)<=1)):
        return encrypted_text
    txt=encrypted_text
    tpt=""
    ops,eps=0,0
    e_num=int (len(txt)/2)
    for lun in range(n):
        even_list,odd_list=txt[:e_num],txt[e_num:]
        for i in range(len(encrypted_text)):
            if i%2==0:
                tpt=tpt+odd_list[ops]
                ops+=1
            else:
                tpt=tpt+even_list[eps]
                eps+=1
        txt=tpt
        ops,eps=0,0
    return txt
        
def encrypt(text, n):
    if ((n<=0)|(len(text)<=1)):
        return text
    for lun in range(n):
        odd_list="".join([text[i] for i in range(len(text)) if (i%2==0)])
        even_list="".join([text[i] for i in range(len(text)) if (i%2!=0)])
        text=even_list+odd_list
    return text

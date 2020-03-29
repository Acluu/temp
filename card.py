k=eval(input())
ls=input().split(' ')
order=[int(i)-1 for i in ls]
huase=['S','H','C','D']
card=[]
for i in huase:
    for j in range(13):
        tpts=i+str(j+1)
        card.append(tpts)
card.append('J1')
card.append('J2')
shuffle=[card[i] for i in range(54)]
for lun in range(k):
    for i in range(54):
        shuffle[order[i]]=card[i]
    card=shuffle.copy()
print(' '.join(shuffle))

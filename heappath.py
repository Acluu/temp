# PTA test datastructure


def insert(x):
    global heap,size
    i=size+1
    size+=1
    while heap[int(i/2)]>x:
        heap[i]=heap[int(i/2)]
        i=int(i/2)
    heap[i]=x


def findpath(loc):
    global heap
    outl=[]
    while loc>=1:
        outl.append(heap[loc])
        loc = int(loc/2)
    print(" ".join([str(i) for i in outl]))


size=0
N,M =[int(i) for i in input().split()]
heap = [i*0 for i in range(N+1)]
heap[0]=-10001
elements = [int(i) for i in input().split()]
for x in elements:
    insert(x)
pathnum = [int(i) for i in input().split()]
for ele in pathnum:
    findpath(ele)

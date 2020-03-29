s=input()
n,m=int(s.split(" ")[0]),int(s.split(" ")[1])
ss=input()
pos=ss.split(" ")
pos=pos[n-m:]+pos[:n-m]
sp=" ".join(pos)
print(sp.strip())

#三个list 1.存放N...1; 2.模拟的栈（最大长度M） 3.比较对象（输入）
#还要整个存结果的list
#处理输入
M,N,K=[int(i) for i in input().split()]
olst=[]
for i in range(K):
    outofM=0
    l1=[N-i for i in range(N)]
    stack=[]
    poi=0
    clst=[int(i) for i in input().split()]
#比较列表的当前位置 不在栈内时 一直压入一个元素直至匹配
#判断栈长度是不是<=M 栈爆了→NO
#在栈中在栈顶吗？→栈顶弹出 更新位置 继续
#else 在栈却不在栈顶 → NO
#最后位置匹配成功 →YES
    while((outofM==0)&(poi<N)):
        while(clst[poi] not in stack):
            stack.append(l1.pop())
        if len(stack)>M:
            olst.append('NO')
            outofM=1
        elif stack[-1]==clst[poi]:
            stack.pop()
            poi+=1
        else:
            olst.append('NO')
            outofM=1
    if (poi==N):
        olst.append('YES')
for s in olst:
    print(s)

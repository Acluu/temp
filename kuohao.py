def valid_parentheses(string):
    Stack=[]
    ostring="".join([i for i in string if i in ['(',')']])
    if ((string is None)|(string=="")):
        return True
    for c in ostring:
        if (Stack==[]):
            Stack.append(c)
            continue
        if ((Stack[-1]=='(')&(c==')')):
            Stack.pop()
        else:
            Stack.append(c)
    return Stack==[]

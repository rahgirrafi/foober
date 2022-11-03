def solution(l):
    from itertools import combinations
    comb = combinations(l,3)
    li=[]
    for x in list(comb):
        li.append(x)
    #print(li)
    s=[]
    for x in li:
        if (x[1]%x[0])== 0:
            if (x[2]%x[1])== 0:
                s.append(x)
                #print(x)

    s.sort()
    print(s)
    n=len(s)
    return n

code = [1,1,2,2,3,3]
print(solution(code))
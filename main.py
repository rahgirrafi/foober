def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                #print l[i], l[j]  # Add () for Python3
                c[i] = c[i] + 1
                count = count + c[j]
                #print count  # Add () for Python3
    return count


q = [1,1,2,2,3,3]
print(solution(q))
#[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,18,18,19,19,20,20,21,21,2,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30]
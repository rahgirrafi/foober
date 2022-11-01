import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def sized_subsets(set, element_number):
    return [x for x in subsets(set) if len(x) == element_number]

def combined_move(list, move_numbers):
    temp = sized_subsets(list, move_numbers)
    unique_n_nth = []
    for i in range(0, ncr(len(list), move_numbers)):
        sum = 0
        j = 0
        for j in range(0, len(temp[0])):
            sum = sum + temp[i][j]
        unique_n_nth.append(sum)
        a = set(unique_n_nth)
    return sorted(a)

sept_move = []
n=1
moves = []
for i in range (0,8):
    sept_move = []
    move = [17, -17, 15, -15, 10, -10, 6, -6]
    move_set = []
    move_set = (sized_subsets(move, n)).copy()

    j=0
    for j in range(0, ncr(8, n)):
        sum=0
        k=0
        for k in range(0, n):
            sum = sum + move_set[j][k]
            sept_move.append(sum)
    n+=1
    moves.append(sept_move)
m = []
for i in range(0, 8):
    temp = set(moves[i])
    m.append(temp)

unique_1= m[0]
unique_2= m[1]-m[0]
unique_3= (m[2]-m[1])-m[0]
unique_4= ((m[3]-m[2])-m[1])-m[0]

unique_1 = sorted(unique_1)
unique_2 = sorted(unique_2)
unique_3 = sorted(unique_3)
unique_4 = sorted(unique_4)

#print(unique_1)
#print(unique_2)
#print(unique_3)
#print(unique_4)


'''
for x in range (1,28):
    unique_2_twice=combined_move(unique_2,x)
    print(f'unique_2_{x}= {unique_2_twice}')
    print()
'''
li=[]
for x in range(56,64):
    li.append(x)
print(li)

















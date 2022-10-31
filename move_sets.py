def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def sized_subsets(set, element_number):
    return [x for x in subsets(set) if len(x) == element_number]

board=[
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22,23],
    [24,25,26,27,28,29,30,31],
    [32,33,34,35,36,37,38,39],
    [40,41,42,43,44,45,46,47],
    [48,49,50,51,52,53,54,55],
    [56,57,58,59,60,61,62,63]
]
print(board[0+1+1][0+1 ])

move_numbers=[]
move=[17,-17,15,-15,10,-10,6,-6]
move_set= sized_subsets(move,4)
for x in move_set:
    move_numbers.append(sum(x))
    move_numbers.sort()
print(move_numbers)



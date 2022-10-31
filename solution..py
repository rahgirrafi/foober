def solution(l):
    def subsets(numbers):
        if numbers == []:
            return [[]]
        x = subsets(numbers[1:])
        return x + [[numbers[0]] + y for y in x]

    def sized_subsets(set, element_number):
        return [x for x in subsets(set) if len(x) == element_number]

    def uni_li(l):
        unique_list = []
        for x in l:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    def number(list):
        p = 0
        number = 0
        for k in reversed(list):
            number = number + k * 10 ** p
            p += 1
        return number

    l.sort(reverse=True)
    total = sum(l)
    if total < 3:
        return 0
    if total % 3 == 0:
        return number(l)

    l.sort()
    subtract_list = uni_li(l)

    # print(f'l = {l}')
    total = sum(l)
    # print(f'total = {total}')
    num = []
    # print(f'subtract_list = {subtract_list}')

    for x in subtract_list:
        if (total - x) % 3 == 0:
            l.remove(x)
            l.sort(reverse=True)
            num = number(l)
            return num
            # print(num)
            # exit()

    for n in range(2, len(l)+1):
        subtract_list = sized_subsets(l, n)
        subtract_list = uni_li(subtract_list)
        subtract_list.sort(key=sum)
        # print(subtract_list)
        for x in subtract_list:
            subtract_number = sum(x)
            if (total - subtract_number) % 3 == 0:
                for j in x:
                    # print(j)
                    l.remove(j)
                    l.sort(reverse=True)
                    num = number(l)
                return num
                # print(num)
                # exit()
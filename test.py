def solution(code):
    def div_and_conq(list, template,ele_value):
        print(f'list inside recursion={list}')
        print(f'temp length inside recursion={len(list)}')
        print(f'final inside recursion ={template}')
        if len(list) == 0:
            print('recursion stopped')
            return {}
        ele = ele_value
        temp = []
        n = int(list[(len(list) - 1)] / ele)
        for x in range(2, n + 1):
            if ele * x in code:
                temp.append(ele * x)
        print(f'temp inside recursion={temp}')
        print(f'making duplets of {ele} and temp= {temp}')
        c = [(ele, b) for b in temp]
        print(f'duplets={c}')
        c = set(c)

        if len(temp) == 0:
            return {}

        return c.union(div_and_conq(temp,template,temp[0]))

    if len(code) == 3:
        if (code[1] % code[0]) == 0:
            if (code[2] % code[1]) == 0:
                return 1
            else:
                return 0
    final = []
    final = set(final)
    for k in code:
        print(f'k={k}')
        ele = k
        temp = []
        n = int(code[(len(code) - 1)] / ele)
        for x in range(2, n + 1):
            if ele * x in code:
                temp.append(ele * x)
        print(f'temp freshly created={temp}')
        if len(temp) < 2:
            break
        for y in temp:
            print((f'len temp ={len(temp)}'))
            if len(temp) > 2:
                a = div_and_conq(temp,final,y)
                print('Exited from recursion')
                print(f'temp right after recursion = {temp}')
                print(f'a={a}')
                a = sorted(a)
            if len(temp) == 2:
                print('merging becuase temp is now 2')
                print(f'temp[0]={temp[0]} and temp[1]={temp[1]}')
                b = (k, temp[0], temp[1])
                final.add(b)
            else:
                print(f'making final elements with {ele} and {a}')
                for x in a:
                    c = list(x)
                    b = (ele, c[0], c[1])
                    final.add(b)
                print(f'final={final}')
    s = []
    for x in final:
        if (x[1] % x[0]) == 0:
            if (x[2] % x[1]) == 0:
               s.append(x)
    n=len(s)
    return n


q = [3,3,6,6,9,9]
print(solution(q))



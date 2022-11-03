def solution(code):
    def div_and_conq(list, template,ele_to_remove):
        #print(f'temp length inside recursion={len(list)}')
        if len(list) == 0:
            ####print('recursion stopped')
            return []
        print(f'list inside recursion={list}')
        #####print(f'final inside recursion ={template}')



        slice_1 = list[:1]
        slice_2 = list[1:]
        print(f'sliced off in recursion silice1= {slice_1}')
        print(f'Other slice in recursion slice2={slice_2}')

        temp = []
        for x in slice_2:
            print(f'checking if {slice_1[0]} can divide {x} or not')
            if x % slice_1[0] == 0:
                temp.append(x)
        print(f'temp inside recursion={temp}')

        print(f"ele_rem ={ele_to_remove}")
        if len(slice_2) > 0:
            ele_to_remove.extend(slice_1)
        print(f'after adding {slice_1}ele_rem={ele_to_remove}')



        if len(temp) == 0:
            return []



        print(f'making duplets of {slice_1[0]} and temp= {temp}')
        c=[]
        for b in temp:
            print('making duplets inside recursion')
            if b % slice_1[0] == 0:
                print(f'{b}%{slice_1[0]}')
                c.extend([(slice_1[0], b)])
        print(f'duplets={c}')
        print('entering deeper recursion')
        c.extend((div_and_conq(temp, template, ele_to_remove)))
        return c


    final=[]
    if len(code)==3:
        if (code[1] % code[0]) == 0:
            if (code[2] % code[1]) == 0:
                #print('returned 1')
                return 1
            else:
                #print('returned 0')
                return 0
    
    #print('started')
    while code[0]*2<= code[-1]:
        #print(f'code= {code}')
        ####print(f'twice of first {code[0]} element is small than last {code[-1]}')
        slice_1= code[:1]
        slice_2=code[1:]
        print(f'sliced off {slice_1}')
        print(f'Other slice {slice_2}')

        temp=[]
        for x in slice_2:
            #print(f'checking if {slice_1[0]} can divide {x} or not')
            if x%slice_1[0]==0:
                temp.append(x)
        #print(f'temp freshly created={temp}')
        ####print('entering loop of temp')

        while True: #recursion loop
            ####print('Looping')
            ####print(f'temp={temp}')
            ####print(f'y = {temp[0]}')
            ####print((f'len temp ={len(temp)}'))
            if len(temp) > 2:
                ele_rem=[]
                a = div_and_conq(temp, final, ele_rem)
                print('Exited from recursion')###################
                print(f'ele_rem={ele_rem}')
                print(f'removed {ele_rem[0]} from ele_rem')
                ele_rem.remove(ele_rem[0])
                print(f'temp = {temp}')
                print(f'removed {temp[0]} temp')
                temp.remove(temp[0])

                for x in ele_rem:
                    delete= False
                    for y in temp:
                        print(f'considering {x} from ele_rem and {y} from temp')
                        if y == x:
                            break
                        elif y%x == 0:
                            print(f'removing {x} from temp={temp}')
                            continue
                        else:
                            delete=True
                    if delete == True:
                       temp.remove(x)
                    #print(f'temp after removing {temp}')

                ##print(f'temp right after recursion = {temp}')
                ####print(f'a={a}')
                a = sorted(a)
                ####print(len(temp))
                ####print(f'making final elements with {slice_1[0]} and {a}')
                for x in a:
                    c = list(x)
                    b = (slice_1[0], c[0], c[1])
                    final.append(b)
                print(f'final={final}')
            if len(temp) == 2:
                #print('checking if mergable or not')
                if temp[1]%temp[0] == 0:
                    #print('merging becuase temp is now 2')
                    #print(f'temp[0]={temp[0]} and temp[1]={temp[1]}')
                    b = (slice_1[0], temp[0], temp[1])
                    final.append(b)
                break
            if len(temp) < 2:
                #####print('breaking loop as temp len is less than 2')
                break
            #else:

        print(f'final= {final}')
        print(f'removed {code[0]} from code')
        code.remove(code[0])
    #final=set(final)
    n=len(final)
    final.sort()
    print(final)
    return n

q = [1,1,2,2,3,3]
print(solution(q))

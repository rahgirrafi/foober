def solution(s):
    from fractions import Fraction
    ####################### defining functions ###########################
    def matrix_add(a, b):
        c = a[:][:]
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][j] = a[i][j] + b[i][j]
        return c

    def transpose_mat(a):
        t = create_matrix(len(a[0]),len(a))
        for i in range(len(a)):
            for j in range(len(a[0])):
                t[j][i] = a[i][j]
        return t

    def matrix_subtract(a, b):
        c = a[:][:]
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][j] = a[i][j] - b[i][j]
        return c

    def matrix_multipy(q, b):
        result = []
        print(len(q))
        for i in range(len(q)):
            row = []
            for j in range(len(b[0])):
                product = 0
                for v in range(len(q[i])):
                    product += q[i][v] * b[v][j]
                row.append(product)
            result.append(row)
        return result

    def create_matrix(rows, cols):
        m = []
        while len(m) < rows:
            m.append([])
            while len(m[-1]) < cols:
                m[-1].append(0)
        return m

    def identity_matrix(n):
        I = create_matrix(n, n)
        for i in range(n):
            I[i][i] = 1
        return I

    def minor_mat(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def det_matrix(m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * det_matrix(minor_mat(m, 0, c))
        return determinant

    def matrix_inverse(m):
        determinant = det_matrix(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            print('hi')
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = minor_mat(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * det_matrix(minor))
            cofactors.append(cofactorRow)
        cofactors = transpose_mat(cofactors)
        print(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def get_Q(markov_chain):
        for i in absorbing_points:
            del markov_chain[i]
            for j in markov_chain:
                del j[i]
        return markov_chain


    def get_R(markov_chain):
        blank = create_matrix(len(q),len(absorbing_points))
        ele=[]
        for i in range(0,len(markov_chain)):
            for j in range(0,len(markov_chain)):
                if i not in absorbing_points and j in absorbing_points:
                    ele.append(markov_chain[i][j])
        t=0
        for j in range(0,len(blank)):
            for k in range(0,len(blank[0])):
                blank[j][k] = ele[t]
                t+=1
        return blank

    ####################### defining class ###########################
    class state:
        def __init__(self, matrix, row, colum):
            self.matrix = matrix
            self.total_proable_change = sum(matrix[row])

            sum_column = 0
            for x in range(0, len(matrix)):
                sum_column = sum_column + matrix[x][colum]
            self.inventory = sum_column

            s = [0] * len(matrix[0])
            for x in range(0, len(matrix[row])):
                if sum(matrix[row]) != 0:
                    s[x] = Fraction(matrix[row][x], sum(matrix[row]))
            self.to_s = s
            route_to = []
            for x in s:
                if x == 0:
                    route_to.append(False)
                else:
                    route_to.append(True)
            self.routeTo_s = route_to

            if True in route_to:
                terminal = False
            else:
                terminal = True
            self.terminal = terminal

    ############################### main program ################################################



    S = [state(s, i, i) for i in range(0, len(s))]
    points = []

    count_terminal_state = 0
    conv_prob_matrix = create_matrix(len(s), len(s))
    conv_prob_matrix2 = create_matrix(len(s), len(s))
    for i in range(0, len(s)):
        if S[i].total_proable_change == 0:
            conv_prob_matrix[i][i] = 1
            conv_prob_matrix2[i][i] = 1

        else:
            conv_prob_matrix[i] = S[i].to_s[:]
            conv_prob_matrix2[i] = S[i].to_s[:]

    absorbing_points = []
    for x in conv_prob_matrix:
        if 1 in x:
            a=x.index(1)
            absorbing_points.append(a)
    absorbing_points.sort(reverse=True)

    anti_absorbe=[]
    for i in range(0,len(conv_prob_matrix)):
        if i not in absorbing_points:
            anti_absorbe.append(i)
    anti_absorbe.sort(reverse=True)


    #print(absorbing_points)


    #print(conv_prob_matrix)

    if len(s) < 3:
        return [1, 1]

    for x in range(0, len(s)):
        if S[x].terminal == True:
            count_terminal_state += 1
            points.append(x)


    q = get_Q(conv_prob_matrix2)
    print(f'q = {q}')

    r = get_R(conv_prob_matrix)






    id_mat = identity_matrix(len(q))
    print(id_mat)
    print(q)
    N = matrix_inverse(matrix_subtract(id_mat, q))

    print(N)
    print(r)
    probablity_matrix = matrix_multipy(N, r)
    print(probablity_matrix)


    dom = []

    for x in probablity_matrix[0]:
        dom.append(x.denominator)
    max_dom = max(dom)
    result = []
    for x in probablity_matrix[0]:
        result.append(int(x * max_dom))
    result.append(max_dom)
    return result


s = [[0, 0, 2, 1, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 3, 0, 0, 0], [0, 0, 0, 2, 0, 0], [4, 0, 0, 1, 0, 0], [1, 0, 4, 0, 0, 0]]

print(solution(s))

def solution(s):
    from fractions import Fraction
    from fractions import gcd
    def transpose_mat(a):
        t = create_matrix(len(a[0]), len(a))
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
        # # print(f'inside minor mat')
        # # print(f'isde= {[row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]} ')
        # # print(f'isde= {[row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]} ')
        # # print(m)
        # # print(f'going out')
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def det_matrix(m):
        if len(m) == 2:
            # # print(f'{m[0][0]} + {m[1][1]} - {m[0][1]} * {m[1][0]}')
            # # print(f'returning {m[0][0] * m[1][1] - m[0][1] * m[1][0]}')

            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        # # print('********************************')
        for c in range(len(m)):
            # # print(f'm = {m}')
            # # print(f'{determinant} * (-1) ** {c} * {m[0][c]}')
            # # print(f'before  calc {determinant}')
            # # print(f'det {det_matrix(minor_mat(m, 0, c))}')
            b = minor_mat(m, 0, c)
            # # print(f'b = {b}')
            d = det_matrix(b)
            # # print(f'd = {d}')
            # # print(f'd2= {((-1) ** c) * m[0][c]}')
            determinant = determinant + ((-1) ** c) * m[0][c] * d
            # # print(f'd3={determinant}')
        # # print('returning')
        return determinant

    def matrix_inverse(m):
        determinant = det_matrix(m)
        # # print(f'Fractioned determinent = {determinant}')
        # # print(m)
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        # # print(determinant)
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = minor_mat(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * det_matrix(minor))
            cofactors.append(cofactorRow)
        cofactors = transpose_mat(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                # print(cofactors[r][c])
                cofactors[r][c] = cofactors[r][c] / determinant

        return cofactors

    def get_Q(markov_chain):
        blank = create_matrix((len(s) - len(absorbing_points)), (len(s) - len(absorbing_points)))
        ele = []
        for i in range(0, len(markov_chain)):
            for j in range(0, len(markov_chain)):
                if i in absorbing_points or j in absorbing_points:
                    continue
                else:
                    ele.append(markov_chain[i][j])
        t = 0
        for j in range(0, len(blank)):
            for k in range(0, len(blank[0])):
                blank[j][k] = ele[t]
                t += 1
        return blank

    def get_R(markov_chain):
        blank = create_matrix(len(q), len(absorbing_points))
        ele = []
        for i in range(0, len(markov_chain)):
            for j in range(0, len(markov_chain)):
                if i not in absorbing_points and j in absorbing_points:
                    ele.append(markov_chain[i][j])
        t = 0
        for j in range(0, len(blank)):
            for k in range(0, len(blank[0])):
                blank[j][k] = ele[t]
                t += 1
        return blank

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
                    # # print(matrix[row][x],sum(matrix[row]))
                    g1 = Fraction(matrix[row][x])
                    g2 = Fraction(sum(matrix[row]))
                    s[x] = Fraction(g1 / g2)
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

    if len(s) == 1:
        return [1, 1]
    S = [state(s, i, i) for i in range(0, len(s))]

    terminal_state_amount = 0
    for x in S:
        if x.total_proable_change == 0:
            terminal_state_amount += 1
    if terminal_state_amount == 1:
        return [1, 1]

    special_case=[]
    if S[0].terminal == True:
        special_case.append(0)
        for i in range(0,terminal_state_amount-1):
            special_case.append(0)
        special_case.append(1)
        return special_case

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
    for i in range(0, len(conv_prob_matrix)):

        if 1 == conv_prob_matrix[i][i]:
            absorbing_points.append(i)
    absorbing_points.sort(reverse=True)

    q = get_Q(conv_prob_matrix2)
    r = get_R(conv_prob_matrix)
    id_mat = identity_matrix(len(q))
    N = matrix_inverse(matrix_subtract(id_mat, q))
    probablity_matrix = matrix_multipy(N, r)
    #print(probablity_matrix)

    for i in range(0,len(probablity_matrix[0])):
        probablity_matrix[0][i]= (probablity_matrix[0][i]).limit_denominator()
    dom = []

    for x in probablity_matrix[0]:
        dom.append(x.denominator)

    lcm = 1
    for i in dom:
        lcm = lcm * i // gcd(lcm, i)

    result = []
    for x in probablity_matrix[0]:
        result.append(int(x * lcm))
    result.append(lcm)
    return result


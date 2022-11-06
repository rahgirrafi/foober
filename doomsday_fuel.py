def solution(s):
    from fractions import Fraction
    def matrix_add(a, b):
        c = a[:][:]
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][j] = a[i][j] + b[i][j]
        return c
    def matrix_subtract(a, b):
        c = a[:][:]
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][j] = a[i][j] - b[i][j]
        return c
    def matrix_multipy(a,b):
        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                product = 0
                for v in range(len(a[i])):
                    product += a[i][v] * b[v][j]
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
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

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
    S = [state(s, i, i) for i in range(0, len(s))]
    points = []
    count_terminal_state=0
    for x in range(0, len(s)):
        if S[x].terminal == True:
            count_terminal_state+=1
            points.append(x)
    def get_Q(markov_chain):
        q = [[0] * (len(markov_chain) - count_terminal_state), [0] * (len(markov_chain) - count_terminal_state)]

        for i in range(0, len(markov_chain)):
            for j in range(0, len(markov_chain)):
                if i in points or j in points:
                    continue
                q[i][j] = S[i].to_s[j]
        return q
    q=get_Q(s)
    id_mat=identity_matrix(len(q))
    def ger_R(markov_chain):
        r = create_matrix(len(q),count_terminal_state)
        #print(r)
        for i in range(0,(len(s)-count_terminal_state)):
            for j in range(0,count_terminal_state):
                r[i][j] = S[i].to_s[len(s)-count_terminal_state+j]
        return r
    N= matrix_inverse(matrix_subtract(id_mat,q))
    r=ger_R(s)
    probablity_matrix= matrix_multipy(N,r)
    r=Fraction(1,8)
    dom=[]
    for x in probablity_matrix[0]:
        dom.append(x.denominator)
    max_dom=max(dom)
    result =[]
    for x in probablity_matrix[0]:
        result.append(int(x*max_dom))
    result.append(max_dom)
    return result
s= [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

print(solution(s))

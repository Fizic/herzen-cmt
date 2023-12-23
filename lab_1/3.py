def gauss_jordan(matrix):
    n = len(matrix)
    for i in range(n):
        for k in range(n):
            if k != i:
                factor = matrix[k][i] / matrix[i][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]
    ans = []
    for i in range(n):
        ans.append(round(matrix[i][-1] / matrix[i][i], 3))
    return ans

a = []
b = []
for i in range(4):
    inp = list(map(float, input().split()))
    a.append(inp)

print(gauss_jordan(a))

def gauss_method(a, b):
    n = len(a[0])
    for k in range(n):
        kk = a[k][k]
        for i in range(n):
            a[k][i] /= kk
        b[k] /= kk

        for i in range(k + 1, n):
            k1 = a[i][k]
            for j in range(k, n):
                a[i][j] -= a[k][j] * k1
            b[i] -= b[k] * k1

    ans = [0] * n
    ans[-1] = b[-1] / a[-1][-1]
    for i in range(n - 2, -1, -1):
        ans[i] = b[i]
        for j in range(i + 1, n):
            ans[i] -= ans[j] * a[i][j]

    for i in range(n):
        ans[i] = round(ans[i], 3)
    return ans


a = []
b = []
for i in range(4):
    inp = list(map(float, input().split()))
    b.append(inp.pop())
    a.append(inp)

print(gauss_method(a, b))

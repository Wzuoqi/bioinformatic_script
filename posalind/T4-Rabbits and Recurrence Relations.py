# 创建时间：2022/4/4 23:18
def Fib(n, k):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(res[-1] + k * res[-2])
    return res


print(Fib(33, 3))

# 创建时间：2022/5/27 10:41
def fib_rab(n, m):
    """
    :param n: target month
    :param m: all rabbits live for m months
    :return: the number of rabbits remain after target month
    """
    res = [0] * m
    # 设置空白固定长度的滑动窗口
    res[0] = 1
    for i in range(n):
        live = sum(res)
        new_born = sum(res[1:])
        res[1:] = res[:-1]
        res[0] = new_born
        # 用数组构造的巧妙的滑动窗口
    return live


print(fib_rab(95, 19))

def fib(n):
    #递归算法
    if n ==1 or n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    # a = 0
    # b = 1
    # x = [a, b]
    #
    # for i in range(n-2):
    #     temp = a
    #     a = b
    #     b = temp+b
    #     x.append(b)
    # return x

print(fib(10))

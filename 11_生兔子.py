def rabbit (n):
    inter = int(n/3)
    num = 2
    for i in range(0,inter):
        num += 2 * (inter-i)
    return num

print(rabbit(3))

# 输入三个整数x,y,z，请把这三个数由小到大输出

x = input("plz input the first number \n")
y = input("plz input the second number \n")
z = input("plz input the third number \n")

p = []

p.append(x)
p.append(y)
p.append(z)

p.sort()

print(p)

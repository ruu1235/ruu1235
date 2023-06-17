a = eval(input())


for i in range(a, a+1):
    b = eval(input())

    tmp = b
    sum = 0
    while tmp != 0:
        sum += tmp % 10
        tmp // 10
    print()
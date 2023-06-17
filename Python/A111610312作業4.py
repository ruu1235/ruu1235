a=b=c=d=0

for i in range(20):
    n = eval(input())
    if n == 1:
        a+=1
    elif n == 2:
        b+=1
    elif n== 3:
        c+=1
    else:
        d+=1
    print("陳時中總票數:",a)
    print("蔣萬安總票數:",b)
    print("黃珊珊總票數:",c)
    print("廢票:",d)

        
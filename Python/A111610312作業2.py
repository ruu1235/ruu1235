a=eval(input("輸入整數"))
b=eval(input("輸入整數"))
i = a
f = b
while a!= 0 and b!=0:
    if b>a:
        b= b%a
    else: 
        a = a%b
if a:
    print("最大公因數:",a)
    i//=a
    # i= i//a
    f//=a
    print("最小公倍數:",a*i*f)
 
if b:
    print("最大公因數",b)
    i//=b
    f//=b
    print("最小公倍數:",b*i*f)




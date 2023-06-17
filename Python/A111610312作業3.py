import random
a=0
b=0

for i in range(6):
    sum1 = int(input("->"))
    a+=sum1
    b += random.randint(1 , 100)
print(a)
print(b)
if a==b:
    print("一樣")
else:
    print("不一樣")




    

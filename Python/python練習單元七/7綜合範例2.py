a = ()
b = ()
print("Creat tuple1:")
while True :
    num = eval(input())
    if num == -9999:
        break
    a += (num ,)

print("Creat tuple2:")
while True :
    num = eval(input())
    if num == -9999:
        break
    b += (num ,)

c = a + b

print(("Combined tuple before sorting:"), c )

d = list(c)
print(("Combined list after sorting:"),sorted(d))


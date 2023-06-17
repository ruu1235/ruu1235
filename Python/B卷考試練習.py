#B卷第一題
"""
import math
PI = math.pi
n = eval(input())

print("Diameter = %.2f"%(n * 2))
print("Perimeter = %.2f"%(n * 2 *PI ))
print("Area = %.2f"%(n ** 2 *PI))
"""
#B卷第二題
"""
a = eval(input())
b = eval(input())
c = input()
ans = 0

if c == "+" : ans = a+b
elif c == "-" : ans = a-b
elif c == "*" : ans = a*b
elif c == "/" : ans = a/b
elif c == "//" : ans = a//b
elif c == "%" : ans = a%b
print(ans)
"""
#B卷第三題
"""
a = eval(input())
ans = 0
for i in range(1 , a+1):
    if i % 5 == 0:
        ans += i
print(ans)
"""
#B卷第四題
'''
a= eval(input())

if a == 0:
    print(0)
else:
    while a != 0:
        print((a % 10),end = '')
        a //= 10
'''
#B卷第五題
'''
def compute(n):
    n1 = 0
    n2 = 1
    print("%d %d"%(n1,n2),end = ' ')
    for i in range(3,n+1):
        n3 = n1 +n2
        print("%d"%(n3),end = ' ')
        n1 = n2
        n2 = n3
num = eval(input())
compute(num)
'''
#B卷第六題
'''
A = 1
J = 11
Q = 12
K = 13
ans = 0
for i in range(5):
    n = eval(input())
    ans += n
print(ans) 
'''
#B卷第七題
'''
n = 26
k = eval(input())
for i in range(k):
    s = input()
    s1 = set(s.lower())
    s1.remove(' ')
    print(len(s1) == n)
'''
#B卷第八題
'''
n = input()
print(n.upper())
print(n.title())
'''
#B卷第九題


    

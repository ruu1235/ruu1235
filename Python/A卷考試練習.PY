#A卷第一題
'''
import math
PI = math.pi
n = eval(input())

print("Diameter = %.2f"%(n*2))
print("Perimeter = %.2f"%(n * 2 *PI ))
print("Area = %.2f"%(n **2 *PI))
'''

#A卷第二題
'''
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
'''
#A卷第三題
'''
a =eval(input())
b = eval(input())
ans = 0

for i in range(a, b+1):
    if i % 2 == 0:
        ans += i
print(ans)
'''
#A卷第四題
'''
n = eval(input())
for i in range(n):
    for j in range(n-i , 1 , -1):
        print((' '),end = '')
    for k in range(0,i*2+1):
        print(('*'),end = '')
    print()
'''


#A卷第五題
'''
def compute(x , y):
    ans = x*y
    print(ans)
a =eval(input())
b =eval(input())
compute(a,b)
'''

#A卷第六題 (hard)
'''
s = []
c = [0]*10

for i in range(10):
    n=eval(input())
    s.append(n)
    c[s.index(n)] += 1 
max = max(c)
print(s[c.index(max)])
print(max)
'''
 
#A卷第七題
'''
a = ()
b = ()
print('Create tuple1:')
while True:
    n = eval(input())
    if n == -9999:
        break
    a += (n,)
print('Create tuple2:')
while True:
    n = eval(input())
    if n == -9999:
        break
    b += (n,)
c = a+b
lst = list(c)
print('Combined tuple before sorting:',c)
print('Combined list after sorting:', sorted(lst))
'''
#A卷第八題
'''
n = input().replace('-','')
if (n.isdigit()):
    print("Valid SSN")
else:
    print("Invalid SSN")
'''

#A卷第九題 (放棄)








    

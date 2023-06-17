a = eval(input())
b = eval(input())
ans = 0

for i in range(a, b+1):
    if i%2==0 :
        ans += i

print(ans)
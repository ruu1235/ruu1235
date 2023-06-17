a = eval(input())
ans = 0

for i in range(1, a+1):
    if i%5 == 0:
        ans += i
print(ans)
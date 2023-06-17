import math
a= eval(input("Enter a number:"))
if a >= 10000001 :
    pay = a * 0.45-1305000
elif a >= 4400000 :
    pay = a *0.4 -805000
elif a >= 2350000 :
    pay = a *0.3 -365000
elif a >= 1170000 :
    pay = a *0.2 -130000
elif a >= 520000:
    pay = a *0.12 -36400
elif a >= 0:
    pay = a*0.05
print(round(pay))


import math

n = eval(input())
s = eval(input())

Area = (n*s*s)/( 4 * math.tan(math.pi/n))
print("%.4f"%(Area))
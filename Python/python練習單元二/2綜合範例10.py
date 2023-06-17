a_side = eval(input())
b_side = eval(input())
c_side = eval(input())

if a_side + b_side > c_side\
   and b_side + c_side > a_side\
   and c_side + a_side  > b_side:
    print(a_side+b_side+c_side)
else :
    print("Invalid")

 

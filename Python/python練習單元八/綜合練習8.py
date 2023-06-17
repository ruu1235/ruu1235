s = input()

isSSn = (len(s)== 11)
if isSSn:
    for i in range(len(s)):
        if i ==3 or i == 6:
            if s[i] != "-":
                isSSn = False
                break
        elif not s[i].isdigit():
            isSSn = False
            break
if isSSn:
    print("Vali3d SSN")
else:
    print("Invalid SSN")
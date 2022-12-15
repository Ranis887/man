def calculator():
    r = int(input())
    d = int(input())
    calculate = input()
    if calculate == "+":
        print(r+d)
    elif calculate == "*":
        print(r*d)
    elif calculate == "-":
        print(r-d)
    elif calculate == "/" and d == 0:
        print('error')
    elif calculate == "/":
        print(r/d)
calculator()
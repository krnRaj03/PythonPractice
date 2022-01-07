
print("Enter 1st number")
inp5=int(input())
print("Enter 2nd number")
inp6=int(input())

print("Enter 1 for +, 2 for -, 3 for * or 4 for /")
inp1= int(input())
inp2= int(input())
inp3= int(input())
inp4= int(input())


def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def multiply(x,y):
    return x*y


def divide(x,y):
    return x/y


if inp1==1:
    print(add(inp5, inp6))
elif inp2==2:
    print(subtract(inp5, inp6))
elif inp3==3:
    print(multiply(inp5, inp6))
elif inp4==4:
    print(divide(inp5, inp6))
else: print("Invalid Input")
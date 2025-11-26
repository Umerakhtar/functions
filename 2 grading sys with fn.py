def a():
    return "your grade is A+"
def b():
    return "your grade is B+"
def c():
    return "your grade is C+"
def d():
    return "your grade is D+"
def f():
    return "your grade is F"

while True:
    mks = int(input("enter your marks out of 100:  "))
    if mks >= 90 and mks <= 100:
        print(a())
    elif mks >= 80 and mks < 90:
        print(b())
    elif mks >= 70 and mks < 80:
        print(c())
    elif mks >= 60 and mks < 70:
        print(d())
    elif mks >= 0 and mks < 60:
        print(f())
    else:
        print("invalid marks entered")
   
    print("do you want to continue? (yes/no):  ")
    cont = input().lower()
    if cont != 'yes':
        break 

print("\nprogram ended\n")

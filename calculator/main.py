OPTIONS="""
Add +
Subtract    - 
Multiply    * 
Divide  /
Square  s
"""
# Fixed at 1 or 2
def get_numbers(count):
    firstnum = int(input("Please enter first number"))
    secondnum=None
    if count==2:
        secondnum=int(input("Please enter second number"))
    return (firstnum, secondnum)
while 1:
    print(OPTIONS)
    choice = input("Please choose an operation to perform")
    if choice == "+":
        x,y=get_numbers(2)
        print("Sum is",x+y)
    elif choice == "-":
        x,y=get_numbers(2)
        print("x-y is",x-y)
    elif choice == "*":
        x,y=get_numbers(2)
        print("Product is",x*y)
    elif choice == "/":
        x,y=get_numbers(2)
        assert(y)
        print("x/y is",x/y)
    elif choice == "s":
        x,_y=get_numbers(1)
        print("The square of the number is",x**2)
    else:
        print("Please choose exactly one of +-*/s")

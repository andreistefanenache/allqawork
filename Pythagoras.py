print("""
Pythagoras' Calculator
Given A**2+B**2 == C**2,
1.	Find the length of A given B and C  
2.	Find the length of B given A and C 
3.	Find the length of C given A and B 
""")
def get_side(name):
    "Get side length for a given name"
    return int(input(f'Please provide the side length of {name}:'))
choice = int(input("Please choose an option"))
if choice == 1:
    B=get_side("B")
    C=get_side("C")
    print("Side A has a length of",(C**2-B**2)**.5)
elif choice == 2:
    A=get_side("A")
    C=get_side("C")
    print("Side B has a length of",(C**2-A**2)**.5)
elif choice == 3:
    A=get_side("A")
    B=get_side("B")
    print("Side C has a length of",(A**2+B**2)**.5)
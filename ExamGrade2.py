
mark=int(input("Please enter your mark: "))
if mark < 1 or mark > 100:
    exit(print('Error: marks must be between 1 and 100'))
level=int(input("Please enter your level: "))
if level not in (1,2):
    exit(print('Level must be either 1 or 2'))
if level == 1:
    if mark < 50:print("Fail")
    elif 50 <= mark <= 60:print("Pass")
    elif 61 <= mark <= 70:print("Merit")
    elif 71 <= mark <= 100:print("Distinction")
elif level == 2:
    if mark < 40:print("Fail")
    elif 40 <= mark <= 50:print("Pass")
    elif 51 <= mark <= 65:print("Merit")
    elif 66 <= mark <= 100:print("Distinction")

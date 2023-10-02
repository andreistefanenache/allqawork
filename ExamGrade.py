mark=int(input("Please enter your exam mark"))
if mark < 1 or mark > 100:
    print('Error: marks must be between 1 and 100')
elif mark < 50:
    print('Fail')
elif 50 <= mark <= 60:
    print('Pass')
elif 61 <= mark <= 70:
    print('Merit')
elif 71 <= mark <= 100:
    print('Distinction')
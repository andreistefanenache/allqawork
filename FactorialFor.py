factorial=1
number=int(input("Please enter your number:"))
for n in range(1,number+1):
    factorial*=n
print(factorial)
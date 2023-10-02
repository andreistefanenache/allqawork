"""
Task 3 - Investment 
1.	Add a new file: Investment.py and make it the startup file.  
2.	Calculates how many years it will take an initial investment of £100 to grow to a target value of £1000 if the interest rate is 10%.
Tip: Do not start writing code until you've a plan of action!
3.	Save and run.   
 """
from math import log
initial=int(input("Please enter your initial investment")) or 100
target=int(input("Please enter your target")) or 1000
interest_rate=float(input("Please enter the yearly interest rate")) or 1.1
print(log(target/initial,interest_rate),"years")
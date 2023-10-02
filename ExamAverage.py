"""
Task 5 - Exam Average  
1.	Add a new file: ExamAverage.py and make it the startup file.  
2.	Code a program that:  
a.	Has code to calculate the average of three exam marks  
b.	If the average mark is: o >= 65 output a "Pass" 
c.	If it is  < 65 output a "Fail"  
3.	In the main body of the program input the marks for a student for Math, English and ICT exams.    
4.	Marks should be an integer between 0 and 100. 
a.	Use a for loop until the user enters a valid mark.
b.	Calculate and display their average mark and overall result.  
c.	Please also display the average mark and print out the average.
5.	Save and run.  
"""
math=int(input("Please enter your Math score"))
english=int(input("Please enter your English score"))
ict=int(input("Please enter your ICT score"))
if max(math,english,ict)>100:
    exit(print("Please check your scores, maximum is 100"))
if min(math,english,ict)<0:
    exit(print("Please check your scores, minimum is 0"))
total=math+english+ict
average=total/3
print("Your average is", average)
if average < 65:
    print("Fail")
else:
    print("Pass")
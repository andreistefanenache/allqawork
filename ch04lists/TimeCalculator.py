OPTIONS="""
Time Calculator DD:HH:MM
1-	Add 2 times   
2-	Find the difference between 2 times  
3-	Convert to Hours  
4-	Convert to Minutes  
5-	Convert Minutes to Time  
6-	Convert Hours to Time  
7-	Convert Days to Time  
8-	Exit  

Enter an option:  
"""
def addtwotimes():
    a_d,a_h,a_m=map(int,input("Please enter time one").split(":"))
    b_d,b_h,b_m=map(int,input("Please enter time two").split(":"))
    d=a_d+b_d
    h=a_h+b_h
    m=a_m+b_m
    h+=m//60
    d+=h//24
    m%=60
    h%=24
    if d > 99:print("Day overflow!")
    print(f"{d:02}:{h:02}:{m:02}")
def finddifference():
    a_d,a_h,a_m=map(int,input("Please enter time start: ").split(":"))
    b_d,b_h,b_m=map(int,input("Please enter time end: ").split(":"))
    d=b_d-a_d
    h=b_h-a_h
    m=b_m-a_m
    h+=m//60
    d+=h//24
    m%=60
    h%=24
    if d<0:print("Day underflow!")
    print(f"{d:02}:{h:02}:{m:02}")
def tohours():
    d,h,m=map(int,input("Please enter time: ").split(":"))
    print(d*24+h+m/60)
def tominutes():
    d,h,m=map(int,input("Please enter time: ").split(":"))
    print(d*24*60+h*60+m)
def minutestotime():
    d=h=0
    m=float(input("Please enter minute count: "))
    h+=m//60
    d+=h//24
    m%=60
    h%=24
    d,m,h=map(round,[d,m,h])
    print(f"{d:02}:{h:02}:{m:02}")
def hourstotime():
    d=m=0
    h=float(input("Please enter hour count: "))
    h,m=int(h),(h-int(h))*60
    h+=m//60
    d+=h//24
    m%=60
    h%=24
    d,m,h=map(round,[d,m,h])
    print(f"{d:02}:{h:02}:{m:02}")
def daystotime():
    h=m=0
    d=float(input("Please enter day count: "))
    d,m=int(d),(d-int(d))*60*24
    h+=m//60
    d+=h//24
    m%=60
    h%=24
    d,m,h=map(round,[d,m,h])
    print(f"{d:02}:{h:02}:{m:02}")
while True:
    print(OPTIONS)
    choice=int(input("Please make your numeric choice: "))-1
    jumpfn=[addtwotimes,finddifference,tohours,tominutes,minutestotime,hourstotime,daystotime,exit]
    jumpfn[choice]()

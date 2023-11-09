class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_=class_
    def average_score(self,t1,t2,t3):
        return (t1+t2+t3)/3
s1=Student("bob",20,"English")
s2=Student("alice",21,"Business")
print(s2.age)
print(s2.average_score(32,33,34))

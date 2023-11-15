class student:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age
    def wanafunzi(self):
        print("Name %s \nCourse: %s \nGender: %s \nAge : %d"
          %(self.name, self.course, self.gender,self.age))

stud1 = student("Erick were", "computer science", "Male", 25)
stud1.wanafunzi()
stud2 = student ("Ann Mungai", "software engineering", "female", 20)
stud2.wanafunzi()
stud3 = student("Edward", "SE", "male", 23 )
stud3.wanafunzi()
stud4 = student("Ali", "NS","male", 23)
stud4.wanafunzi()
stud5 = student("liz", "SE", "female", 25)
stud5.wanafunzi()
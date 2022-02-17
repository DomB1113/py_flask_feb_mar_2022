class Classroom:
    def __init__(self,subject,time_to_meet,class_size,is_online):
        self.subject = subject
        self.time_to_meet = time_to_meet
        self.class_size = class_size
        self.is_online = is_online
        self.students = [] # Empty list initially that will eventually hold Students

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.classrooms = [] # Empty list that will hold Classrooms

coding_classroom = Classroom("Python","5 PM Pacific",100,True)
math_classroom = Classroom("Mathematics","1 PM Pacific", 30, False)

adrian = Student("Adrian",50)
kim = Student("Kim",30)

# Linking students to a classroom
coding_classroom.students.append(adrian)
coding_classroom.students.append(kim)

# Linking classrooms to a student
adrian.classrooms.append(coding_classroom)
kim.classrooms.append(coding_classroom)

# Show all the students in the Coding Classroom - by looping through the list of Students
for x in coding_classroom.students: # x is NOT an index - it's the actual Student object (instance)
    print(x.name) # Now you can access any attributes or methods in the Student class

from student import Student
from college import College

#Create College with capacity 2
c = College(2)

#Create Students
s1 = Student(1, 'Riya', 20, 75)
s2 = Student(2, 'Amit', 21, 65)

#Add Students
c.addStudent(s1)
c.addStudent(s2)

#Display all students
print(c)

#Get Student
s = c.getStudent(1)
print('\nFound:', s)

#Remove Student
c.removeStudent(1)

#Display again
print('\nAfter Removal:')
print(c)

from student import Student

print('--- Student Management System ---')

n = int(input('Enter number of students: '))

for i in range(n):
    print(f'\n--- Enter Details of Student {i+1} ---')
    
    s = Student()
    s.accept()
    
    print('\n--- Result ---')
    s.display()

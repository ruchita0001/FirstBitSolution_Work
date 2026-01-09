#Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Input marks for 5 subjects
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

# Calculate total marks
total_marks = m1 + m2 + m3 + m4 + m5 

# Assuming maximum marks is 500 (100 for each subject)
max_marks = 500

# Calculate percentage
percentage = (total_marks / max_marks) * 100

# Display results
print("total_Marks:", total_marks)
print("max_marks:", max_marks)
print("percentage:", int(percentage), "%")
# Ask student to input the number of courses
num_courses = int(input("Enter the number of courses: "))

# Initialize variables
total_points = 0
total_credits = 0

# Loop through each course
for i in range(num_courses):
    # Ask the user to input the grade and credit for the course
    grade = (input("Enter the grade for course {}: ".format(i + 1)))
    credits = int(input("Enter the credit for course {}: ".format(i + 1)))


# Calculate the grade points and add them to the total
    if grade == "A":
        grade_points = 5.0
    elif grade == "B":
        grade_points = 4.0
    elif grade == "C":
        grade_points = 3.0
    elif grade == "D":
        grade_points = 2.0
    elif grade == "F":
        grade_points = 0
    else:
        grade_points = 0.0
    total_points += grade_points * credits

    # Add the credits to the total
    total_credits += credits

# Calculate the GPA and print it
gpa = total_points / total_credits
print("Your GPA is {:.2f}".format(gpa))

if gpa > 4.5:
    print("CONGRATULATIONS!! YOU ARE A GENIUS")

if gpa >= 3.0:
   print("YOU DID WELL!")

if gpa <= 2.0:
   print("Try harder next time")

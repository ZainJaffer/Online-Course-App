from student import Student
from course_platform import CoursePlatform
import json

def save_students_to_file(students, filename='students_data.json'):
    students_data = [student.to_dict() for student in students]
    
    with open(filename, 'w') as file:
        json.dump(students_data, file, indent=4)

def main_menu():
    print("Welcome to the Course Platform!")
    while True:
        print()
        print("1. Register")
        print("2. Log in")
        choice = input("Please choose an option (1 or 2): ")
        
        try:
            choice = int(choice)
      
            if choice == 1:
                print("You will be registered into the Udemy course platform.")
                register(udemy)
                
            elif choice == 2:
                print("You chose to log in.")
                break
            else:
                print("Invalid choice. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

def register(udemy):
    first_name = input("Please type in your first name: ").title()
    last_name = input("Please type in your last name").title()
    full_name = first_name + " " + last_name
    full_name = Student(name=full_name)
    udemy.register_student(full_name)
    password = input("Please choose a password")
    full_name.password = password
    
    # Save the students after registration
    save_students_to_file(udemy.all_students)

def enroll():
    pass


udemy=CoursePlatform()
  
main_menu()
udemy.list_students()



# python_course = PaidCourse('Intro to Python Coding','Angela Yu', 90, 30)
# java_course = FreeCourse('Intro to Java Coding', 'Bob Milk', 10)







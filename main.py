import json

def save_students_to_file(students, filename='students_data.json'):
    students_data = [student.to_dict() for student in students]
    
    with open(filename, 'w') as file:
        json.dump(students_data, file, indent=4)

class Course:
    def __init__(self, title, instructor, duration, price, status=True):
        self.title = title
        self.instructor = instructor
        self.duration = duration
        self.price = price
        self.status = status

    def to_dict(self):
       
       return {
        'title' : self.title,
        'instructor': self.instructor, 
        'duration': self.duration, 
        'price' : self.price, 
        'status' : self.status 
        }

    def get_details(self):
        return self.to_dict()

    def cancel_course(self):
        self.status = False

class FreeCourse(Course):
    def __init__(self, title, instructor, duration, price=0):
        super().__init__(title, instructor, duration, price)

class PaidCourse(Course):
    def __init__(self, title, instructor, duration, price):
        super().__init__(title, instructor, duration, price)

class PremiumCourse(Course):
    def __init__(self, title, instructor, duration, price):
        super().__init__(title, instructor, duration, price)

class Student:
    def __init__(self, name, password=""):
        self.enrolled_courses = {}
        self.name = name
        self.password = password

    def enroll(self,course):
        self.enrolled_courses.update({course.title : course})
 
    def cancel_enrollment(self, course):
        del self.enrolled_courses[course.title]

    def list_courses(self):
        course = self.enrolled_courses
        for keys in course:
            print(f"{course[keys].title}: {course[keys].instructor}, {course[keys].duration} days for ${course[keys].price}") if course[keys].status else print("Sorry course is no longer active")

    def to_dict(self):
        return {
            'name': self.name,
            'password': self.password,
            'enrolled_courses': {title: course.to_dict() for title, course in self.enrolled_courses.items()}
        }

class CoursePlatform:
    def __init__(self, course=0):
        self.course = course
        self.all_courses = {}
        self.all_students = []

    def add_course(self, course):
        self.all_courses.update({course.title : course})

    def remove_course(self,course):
        del self.all_courses[course.title]

    def list_courses(self):
        if len(self.all_courses) == 0:
            print("There are no classes on the platform")
        else:     
            for value in self.all_courses.values():
                print(f"{value.title} : {value.instructor}, {value.duration} days for ${value.price}, Active: {value.status}")

    def register_student(self, *student):
        for names in student:
            self.all_students.append(names)
            print(f"Registered: {names.name}")

    def list_students(self):
        print("Here are the list of students:")
        counter=0
        for student in self.all_students:
            counter+=1
            print(f"{counter}. {student.name}")

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


udemy=CoursePlatform()
  
main_menu()
udemy.list_students()



# python_course = PaidCourse('Intro to Python Coding','Angela Yu', 90, 30)
# java_course = FreeCourse('Intro to Java Coding', 'Bob Milk', 10)







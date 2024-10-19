class Course:
    def __init__(self, title, instructor, duration, price, status=True):
        self.title = title
        self.instructor = instructor
        self.duration = duration
        self.price = price
        self.status = status

    def get_details(self):
       
       return {
        'title' : self.title,
        'instructor': self.instructor, 
        'duration': self.duration, 
        'price' : self.price, 
        'status' : self.status 
        }

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
    def __init__(self, name):
        self.enrolled_courses = {}
        self.name = name

    def enroll(self,course):
        self.enrolled_courses.update({course.title : course})
 
    def cancel_enrollment(self, course):
        del self.enrolled_courses[course.title]

    def list_courses(self):
        course = self.enrolled_courses
        for keys in course:
            print(f"{course[keys].title}: {course[keys].instructor}, {course[keys].duration} days for ${course[keys].price}") if course[keys].status else print("Sorry course is no longer active")

class CoursePlatform:
    def __init__(self, course=0, students=0):
        self.course = course
        self.students = students
        self.all_courses = {}
        self.students = []

    def add_course(self, course):
        self.all_courses.update({course.title : course})

    def remove_course(self):
        pass

    def list_courses(self):
        for value in self.all_courses.values():
            print(f"{value.title} : {value.instructor}, {value.duration} days for ${value.price}, Active: {value.status}")

    def register_student(self, student):
        self.students.append([student.name])

    def list_students(students):
        for key in students:
            print(key)

python_course = PaidCourse('Intro to Python Coding','Angela Yu', 90, 30)
java_course = FreeCourse('Intro to Java Coding', 'Bob Milk', 10)

zain=Student('Zain Jaffer')

zain.enroll(python_course)
zain.enroll(java_course)

zain.cancel_enrollment(python_course)


udemy = CoursePlatform()
udemy.add_course(python_course)
udemy.list_courses()
udemy.register_student(zain)
udemy.list_students()

"""

Student Class:

Attributes: name, enrolled_courses (a dictionary of courses the student is enrolled in)
Methods:
enroll(course): Enroll the student in a course.
cancel_enrollment(course): Cancel enrollment in a course.
list_courses(): List all courses the student is enrolled in.
CoursePlatform Class:

Attributes: courses (dictionary of available courses), students (dictionary of registered students)
Methods:
add_course(course): Add a course to the platform.
remove_course(course): Remove a course from the platform.
list_courses(): List all available courses.
register_student(student): Register a student on the platform.
list_students(): List all registered students.
Example Repeated Problems:
Student Enrollments:

Practice enrolling multiple students in various courses.
Repeat adding, removing, and canceling enrollments to get comfortable with dictionary operations.

Course Management:

Add, remove, and manage multiple courses. 
You’ll practice inheritance and repeatedly work with different course 
types (Free, Paid, Premium).

Listing and Viewing Details:

Implement list_courses() and list_students() repeatedly 
across different classes, ensuring that all data 
is displayed in a structured way."""


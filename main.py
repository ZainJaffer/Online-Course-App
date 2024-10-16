class Course:
    def __init__(self, title, instructor, duration, price):
        self.title = title
        self.instructor = instructor
        self.duration = duration
        self.price = price

    def get_details(self):
        pass

    def cancel_course(self):
        pass

class FreeCourse(Course):
    def __init__(self, title, instructor, duration, price):
        super().__init__(title, instructor, duration, price)

class PaidCourse(Course):
    def __init__(self, title, instructor, duration, price):
        super().__init__(title, instructor, duration, price)

class PremiumCourse(Course):
    def __init__(self, title, instructor, duration, price):
        super().__init__(title, instructor, duration, price)

class Student:
    def __init__(self, name, enrolled_courses):
        pass

    def enroll(self,course):
        pass

    def cancel_enrollment(self, course);
        pass

    def list_courses(self):
        pass

class CoursePlatform:
    def __init__(self, courses, students):
        pass

    def add_course(self):
        pass

    def remove_course(self):
        pass

    def list_courses(self):
        pass

    def register_student(self, student):
        pass

    def list_students():
        pass
        
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


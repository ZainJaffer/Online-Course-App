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
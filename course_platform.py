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

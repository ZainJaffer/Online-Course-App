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

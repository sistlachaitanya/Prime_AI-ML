class Employee:
    start_time = "11:00 am"
    end_time = "7:00 pm"

    def __init__(self, shift):
        self.shift = shift


class Developer(Employee):

    def __init__(self, role, shift):
        super().__init__(shift)
        self.role = role


class Teacher(Employee):
    

    def __init__(self, subject, shift):
        super().__init__(shift)
        self.subject = subject


d1 = Developer("Full Stack Developer", "day")
t1 = Teacher("Mathematics", "night")

print(d1.role, d1.start_time, d1.end_time, d1.shift)
print(t1.subject, t1.start_time, t1.end_time, t1.shift)

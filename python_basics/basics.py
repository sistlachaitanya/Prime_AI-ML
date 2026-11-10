class Student:
  def __init__(self, name, cgpa):
    self.name = name
    self.cgpa = cgpa

  def get_cgpa(self):
    return self.cgpa

  college = "ABC College"

stu1 = Student("Rama", 16)

print(f"Name: {stu1.name}\nCgpa:{stu1.get_cgpa()}\nCollege: {stu1.college}") 
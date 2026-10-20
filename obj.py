class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks



s1 = Student(1, "Jay", 68)
s2 = Student(10, "Pavan", 88)
s3 = Student(6, "Viru", 98)
s4 = Student(4, "Priya", 58)
s5 = Student(11, "Payal", 78)

student_list = []

student_list.append(s1)
student_list.append(s2)
student_list.append(s3)
student_list.append(s4)
student_list.append(s5)

for obj in student_list:
    if obj.marks > 75:
        print(obj.name, obj.marks)
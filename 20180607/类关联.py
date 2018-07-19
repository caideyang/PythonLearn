#encoding:utf-8

class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr


class Teacher:
    def __init__(self,name,salary,school):
        self.name = name
        self.salary = salary
        self.school = school

class Course:
    def __init__(self,name,period,fee,school,teacher):
        self.name = name
        self.period = period
        self.fee = fee
        self.school = school
        self.teacher = teacher



if __name__ == "__main__":
    school1 = School('oldboy','北京校区')
    school2 = School('oldboy','南京校区')
    school3 = School('oldboy','天津校区')
    print("""
        1: 北京校区
        2：南京校区
        3：天津小区
        4：退出
    """)
    teacher1 = Teacher('张1',10000,school1)
    teacher2 = Teacher('张2',10000,school1)
    teacher3 = Teacher('张3',10000,school1)
    teacher4 = Teacher('张4',10000,school2)
    teacher5 = Teacher('张5',10000,school2)
    teacher6 = Teacher('张6',10000,school2)
    teacher7 = Teacher('张7',10000,school3)
    teacher8 = Teacher('张8',10000,school3)
    teacher9 = Teacher('张9',10000,school3)

    while True:
        school = input("School>>> ")
        
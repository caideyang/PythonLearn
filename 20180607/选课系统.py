#encoding:utf-8

import pickle,time,hashlib
import os

#创建随机编号
def create_id():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()

#获取文件内容

class Base:
    def save(self):
        with open(self.cls+"/"+self.id ,'wb' ) as f:
            pickle.dump(self,f)

class School(Base):
    cls = 'school'
    def __init__(self,name,addr):
        self.id = create_id()
        self.name = name
        self.addr = addr

class Teacher(Base):
    cls = "teacher"
    def __init__(self,name,salary,school):
        self.name = name
        self.salary = salary
        self.school = school

class Course(Base):
    cls = 'course'
    def __init__(self,name,price,period,teacher,school):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher
        self.school = school


class Student(Base):
    cls = "student"

class ClassRoom(Base):
    cls = 'classroom'

if __name__ == "__main__":

    menu = """
        0-创建学校
        1-创建老师
        2-创建课程
        3-创建班级
        4-创建学生
        q-退出
    """
    def create_school():
        name = input("请输入学校名称:").strip()
        addr = input("请输入校区地址：").strip()
        School(name,addr).save()

    def create_course():
        name = input("请输入课程名称:").strip()

    def create_teacher():
        name = input("请输入老师名称:").strip()


    while True:
        print(menu)
        choice = input(">>> ").strip()
        if choice.upper() == 'Q':break
        elif choice == '0': create_school()


    # s1 = School('老男孩','南京校区')
    # s1.save()
    file_name = os.listdir('school')
    for file in file_name:
        school = pickle.load(open('school/'+file,'rb'))
        print(school.__dict__)
        print(school.id,school.name,school.addr)
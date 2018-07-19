#encoding:utf-8

"""
1.可进行模糊查询，语法至少支持下面3种查询语法
2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
3.可删除指定员工信息纪录，输入员工id，即可删除
4.可修改员工信息，语法如下:
5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、
修改语句就显示修改了多少条等。
要充分使用函数，请尽你的最大限度来减少重复代码！
staff_id,name,age,phone,dept,enroll_date
1,王五,25,157016802,Market,2015-10-14
2,赵六,33,158206312,Market,2005-09-27
3,孙七,24,137338110,Market,2014-06-23
4,zengchuixin,22,12378902792,Market,2014-06-23
5,zengchuixin,22,12378902904545,Market,2014-06-23
6,zengchuixin,22,4445555,IT,2014-06-23
"""
#从文件中获取员工信息
def get_info(file="employee.info"):
    employee_info = []
    with open(file,'r',encoding='utf-8') as f:
        employees = f.readlines()
        for employee in employees:
            employee_info.append(employee.split(","))
    return employee_info

#保存员工信息到表中
def save_info(employee_info,file="employee.info"):
    with open(file, 'w+', encoding='utf-8') as f:
        for employee in employee_info:
            f.write(employee)
    print("Success saved！")

def compare():
    pass

#查询
def select(employee_info):
    command = input("请输入查询语句：")
    while True:
        results = []
        com_list = command.split()
        print(com_list)
        if com_list[5] not in employee_info[0]:
            print("表中无对应字段%s" %com_list[5] )
            break
        else:
            condition_index = employee_info[0].index(com_list[5])
            if com_list[6] == '<':
                for employee in employee_info[1:]:
                    if int(employee[condition_index]) < int(com_list[7]):
                        results.append(employee)
            elif com_list[6] == '=':
                for employee in employee_info[1:]:
                    if int(employee[condition_index]) == int(com_list[7]):
                        results.append(employee)
            elif com_list[6] == '>':
                for employee in employee_info[1:]:
                    if int(employee[condition_index]) > int(com_list[7]):
                        results.append(employee)
            elif com_list[6] == 'like':
                for employee in employee_info[1:]:
                    if com_list[7] in employee[condition_index]:
                        results.append(employee)
        if com_list[1] == "*":
            field_list = employee_info[0]
            print("共查到%s条结果，如下：" % len(results))
            for result in results:
                print(result)
            break
        else:
            field_list = com_list[1].split(",")
            for field in field_list:
                if field not in employee_info[0]:
                    print("列表中无对应字段%s" % field)
                    break









if __name__ == "__main__":
    employee_info = get_info()
    select(employee_info)

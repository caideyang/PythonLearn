#encoding:utf-8
import sys,os,re

#获取文件内容
def get_content(filename):
    with open(filename,"r",encoding="utf-8") as f:
        content = f.readlines()
    return content

#保存文件内容
def save_content(filename,content):
    with open(filename,'a+',encoding="utf-8") as f:
        for line in content:
            f.write(line)

def select(content):
    res = []
    while content:
        condition = input("请输入要查询的内容(q退出，b返回)：").strip()
        if condition.upper() == 'Q':exit()
        if condition.upper() == 'B':break
        for line in content:
            if condition in line:
                res.append(line)
    else:
        print("当前文件内容为空")
    return res

def insert(filename):
    pass

def update(content):
    select_result = select(content)
    while select_result:


def delete(filename):
    pass




if __name__ == "__main__":
    menu = """
    1 --》 查询
    2 --》 插入
    3 --》 修改
    4 --》 删除
    q --》 退出
    b --》 上一级
    """
    while True:
        filename = input("请输入你要操作的文件: ").strip()
        if filename.upper() == "Q": break
        if os.path.exists(filename):
            content = get_content(filename)
            print("当前需要操作的文件%s" % filename)
        else:
            print("文件不存在")
            continue
        while True:
            print(menu)
            choise = input("请输入要做的操作：").strip()
            if choise == '1' : select(content)
            elif choise == '2' : insert(content)
            elif choise == '3' : update(content)
            elif choise == '4' : delete(content)
            elif choise.upper() == 'B': break
            elif choise.upper() == 'Q': exit()
            else: print("输入有误，请重新输入！")



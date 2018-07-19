# from module.test import add
#
# print(add.add(1,5))
#
# print(__name__)


import random
#获取验证码函数
def vote(n):
    vote_code = ""
    if n < 1:
        print("Error:验证码长度有误!")
        exit(-1)
    for i in range(n):
        number = random.randint(0,9)
        letter = chr(random.choice([random.randint(65,90),random.randint(97,122)]))
        if letter == 'l':
            letter == 'L'
        vote_code += str(random.choice([number,letter]))
    return vote_code

if __name__ == "__main__":
    tag = True
    while tag:
        vote_code  = vote(6)
        vote_number = input("Pls. insert your vote code [%s]: " %vote_code)
        if vote_code.upper() == vote_number.upper():
            print("输入正确，登陆成功！")
            tag = False
        else:
            print("验证码错误，请重新输入！")

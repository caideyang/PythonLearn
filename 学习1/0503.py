#encoding:utf-8
# https://github.com/eclipse/paho.mqtt.python

# while True:
#     value = input(">>>")
#
# # mod = str.maketrans("苍井空东京热","******")
# # new_value = value.translate(mod)
# # print(new_value)
#     if value.upper() == "Q":
#         break
#     print(value.replace("苍井空","***").replace("苍老师","***").replace("东京热","***"))

import random

while True:
    code_number = random.randint(100000,999999)
    print("当前验证码是%d" % code_number)
    vcode_number = int(input("Pls. insert your vcode: "))
    if vcode_number == code_number:
        print("验证成功！")
        break
    else:
        print("验证失败，重新验证！")




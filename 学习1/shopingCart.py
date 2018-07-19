#encoding:utf-8

"""
需求：
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
"""
import json,datetime

# 自定义错误提示信息
error_info = '输入有误，请检查后重新输入！'

#saveAccount函数 用于将购物相关信息保存到JSON文件，比如用户信息,购物列表，账户余额
def saveAccount(database, filename='user_info.json'):
    # 打开并可写文件,若文件已存在，则以前的内容将被清除
    # 使用with as语句的效率更高，不需要单独设置如何读文件之后再如何关闭文件，一个with as搞定所有读写关闭操作
    with open(filename,'w') as f:
        json.dump(database,f)

# 定义loadDatabase函数,从json文件中读取信息
def loadDatabase(filename='user_info.json'):
    with open(filename) as f:
        database = json.load(f)
    return database

# 定义一个函数setShoppingTime,格式化时间
def setShoppingTime():
    shopping_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return shopping_time

# 函数getShoppingHistory，用于查询购物历史记录
def getShoppingHistory(account):
    database = loadDatabase()
    records = database[account]['shopping_list']
    for record in records:
        print('您于%s购买了%s件%s,单价%s元，总价%s元' %(record["shopping_time"],record["num"],record["product"],record["singlePrice"],record["totalCost"]))

#函数operation用于登陆后的操作
def operation(account):
    command = input('按h查询购物历史,按s开始购物,按t充值,按q退出:').strip()
    database = loadDatabase()
    if command.upper() == 'H':
        if database[account]['shopping_list'] != []:
            # 输出购物历史信息
            getShoppingHistory(account)
        else:
            print('您在本商城没有购买过东西！')
    elif command.upper() == 'T':
        recharge(account)
    elif command.upper() == 'S':
        shopping(account)
    elif command.upper() == 'Q':
        logout(account)
    else:
        print(error_info)
# 定义一个函数login，用于登录系统
def login():
    database = loadDatabase()
    blacklist = loadDatabase('BlackList.json')
    print('欢迎登录购物系统！')
    while True:
        account = input("请输入您的账号登录系统（按q退出）：")
        if account in blacklist:
            print("您的账号已经被锁定，请联系管理员处理！")
            logout()
        elif account.upper() == 'Q':
            logout()
        # 这里使用while循环和count计数器，如果输入错误密码大于3次，则锁定账户
        elif account in database:
            count = 0
            while count < 3:
                pwd = input('请输入密码：')
                if pwd == database[account]['pwd']:
                    while True:
                        # 登录成功后，通过getAccountBalance函数得到登陆用户余额
                        account_balance = getAccountBalance(account)
                        if account_balance == 0:
                            print('您的账户余额是\033[32m%d\033[0m,必须充值！'% account_balance)
                            recharge(account)
                        print('您的账户余额是\033[32m%d\033[0m' % account_balance)

                        operation(account)
                else:
                    count += 1
                    print('输入的密码错误，你还有%s机会' % (3 - count))
            # 将用户账号添加至blacklist,保存成字典形式,value设置为None
            # 这里使用了字典的setdefalut用法，如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值
            blacklist.setdefault(account)
            # 用户输入三次错误操作之后，会跳出while循环，告诉用户账号已锁定
            print('您的账号已经锁定！')
            saveAccount(blacklist,'BlackList.json')
            logout()
        else:
            print('账号不存在，请重试！或输入b返回上一层，输入q，退出购物程序！')

# 函数setShoppingList，用于存放购物记录
def setShoppingList(account, p_name, num, singlePrice, totalCost, shopping_time):
    shopping_record = {"product":p_name,"num":num,"singlePrice":singlePrice,"totalCost":totalCost,"shopping_time": shopping_time}
    database = loadDatabase()
    database[account]["shopping_list"].append(shopping_record)
    saveAccount(database)

# 函数setBalance，计算购买商品后账户所剩下的余额
def setBalance(account,num):
    database = loadDatabase()
    # 购买商品后，扣除购买的商品的价格
    database[account]['balance'] -= num
    saveAccount(database)

# 定义一个函数，用于执行充值操作
def recharge(account):
    database = loadDatabase()
    while True:
        num = input('请输入您要充值的金额:')
        if num.isdigit():
            database[account]["balance"] += int(num)
            saveAccount(database)
            account_balance = getAccountBalance(account)
            # 高亮打印充值后的余额信息
            print('您已成功充值,您的余额为\033[32m%d\033[0m元' % account_balance)
            return None
        else:
            print('您的输入有误,请重新输入!')

# 函数getAccountBalance，用于获取账户余额
def getAccountBalance(account):
    database = loadDatabase()
    return database[account]['balance']

# 函数shopping，用于执行购物程序
def shopping(account):
    goods = [
                {"name": "电脑", "price": 1999},
                {"name": "鼠标", "price": 100},
                {"name": "游艇", "price": 20000},
                {"name": "美女", "price": 9998},
                {"name": "粪叉", "price": 8388},
    ]
    while True:
        print("商品列表".center(50, "-"))
        print("编号".center(8, " "), "名称".ljust(30, " "), "价格".ljust(10, " "))
        for i in enumerate(goods):
            print(str(i[0]).center(10, " "), i[1]['name'].ljust(30, " "), str(i[1]['price']).ljust(10, " "))
        while True:
            p_id = input("请输入您要选择的产品编号(输入q退出,输入h查询购物历史，输入s再次获取商品列表):").strip()
            if p_id.upper() == 'Q': logout(account)
            elif p_id.upper() == 'S':break
            elif p_id.upper() == 'H':
                database = loadDatabase()
                if database[account]['shopping_list'] != []:
                    getShoppingHistory(account)
                else:
                    print('您在本商城没有购物记录！')
            elif p_id not in map(str,range(len(goods))):
                print("无对应商品，请重新输入！")
                break
            # 如果用户输入的商品名称在所选择的商品列表中
            else:
                while True:
                    p_id = int(p_id)
                    p_name = goods[p_id]['name']
                    num = input('请输入要购买的商品"%s"的数量:' %p_name).strip()
                    if num.isdigit():
                        num = int(num)
                        if num == 0:
                            print("您未购买%s ，请重新选择要购买的商品!" %p_name)
                            break
                        account_balance = getAccountBalance(account)
                        # 商品单价
                        singlePrice = goods[p_id]['price']
                        # 商品总价
                        totalCost = singlePrice * num
                        if account_balance >= totalCost:
                            # 调用setBalance函数，计算购买后的账户余额是多少
                            setBalance(account, totalCost)
                            # 购物时间
                            shopping_time = setShoppingTime()
                            print('您成功购买%d件商品:%s!' % (num, p_name))
                            # 调用setShoppingList函数，将购买的商品列表保存到json文件中
                            setShoppingList(account, p_name, num, singlePrice, totalCost, shopping_time)
                            # 定义account_balance变量，通过使用getAccountBalance函数重新获取账户的余额信息
                            account_balance = getAccountBalance(account)
                            print('您目前的账户余额为\033[31m%d\033[0m元' % account_balance)
                            # 退出当前的循环，到上一级循环，用户可以选择是否继续购物
                            break
                        else:
                            print('您的账户余额不足！')
                            g = input("充值输入t，返回上一级输入b，退出输入q':")
                            if g.upper() == 'Q':
                                logout()
                            if g.upper() == 'B':
                                break
                            if g.upper() == 'T':
                                recharge(account)
                    else:
                        print(error_info)

# 设置默认变量account = None来判定账号是否已经登录,如果没有登录就退出,则不打印购物信息
# 如果已经登录过，则打印购物历史信息
def logout(account=None):
    if account != None:
        getShoppingHistory(account)
    exit('感谢您来购物!')
if __name__ == '__main__':
    while True:
        login()
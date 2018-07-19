#encoding:utf-8

user_dict = {'username':None ,'login':False}

#装饰器函数，判断访问用户是否登陆
def user_auth_func(auth_type="text"):
    def user_auth(func):
        def wrapper(*args,**kwargs):
            if user_dict['username'] and user_dict['login']:
                res = func(*args, **kwargs)
            else:
                print("用户未登陆登陆！请登陆...")
                username = input("Username: ")
                passwd = input("Password: ")
                if username == "cdy" and passwd == "123456":
                    user_dict['username'] = username
                    user_dict['login'] = True
                    print("用户%s登陆成功！" % user_dict['username'])
                    res = func(*args, **kwargs)
                else:
                    print("用户名或密码错误！")
                    exit()
            return res  # 访问登陆用户当前的页面

        return wrapper
    return user_auth

@user_auth_func(auth_type="text")
def index(*args,**kwargs):
    print("当前是index页面")
    return args,kwargs

@user_auth_func(auth_type="text")
def home(*args,**kwargs):
    print("当前是home页面")
    return args, kwargs

@user_auth_func(auth_type="text")
def shopping_car(*args,**kwargs):
    print("当前是shopping_car页面")
    print("购物车里商品是：%s" %str(args))
    return args, kwargs

@user_auth_func(auth_type="text")
def order(*args,**kwargs):
    print("当前是order页面")
    return args, kwargs

shopping_car(*("年差","每每"))
index()
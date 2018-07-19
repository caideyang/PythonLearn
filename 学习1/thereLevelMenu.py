#encoding:utf-8
"""
作业题目: 三级菜单

需求：
可依次选择进入各子菜单
可从任意一层往回退到上一层
可从任意一层退出程序
所需新知识点：列表、字典
"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
def getlevel(menu):
    while True:
        if len(menu) == 0: print("The end level !")
        for key in menu:
            print(key)
        choise = input("Pls. insert your choise:(\"Q\" for exit,\"B\" for back.) ")
        if choise == "Q":
            exit("Exit !")
        elif choise == "B":
            break
        elif choise not in menu:
            choise = input("Pls. insert your choise:(\"Q\" for exit,\"B\" for back.) ")
        else:
            getlevel(menu[choise])

if __name__ == "__main__":
    getlevel(menu)

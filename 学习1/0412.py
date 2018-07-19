#encoding:utf-8

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
        print(str(i[0]).center(10, " "), str(i[1]['name']).ljust(30, " "), str(i[1]['price']).ljust(10, " "))
    while True:
        p_id = input("请输入您要选择的产品编号(输入b返回,输入q退出):").strip()
        if p_id.upper() == 'Q':pass
        if p_id.upper() == 'B': break

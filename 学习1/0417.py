#encoding:utf-8
# from io import StringIO
# f = StringIO()
# f.write("Hello1\n")
# f.write("Hello2\n")
# f.write("Hello3\n")
# print(f.getvalue())
#
#
#
# from io import StringIO
# f = StringIO("Hello1\nWorld\n!")
# while True:
#     content = f.readline()
#     if content == "":
#         break
#     print(content.strip())
#
#
#
# from io import BytesIO
# f = BytesIO()
# f.write(b'\xe4\xb8\xad\xe5\x9b\xbd')
# print(f.getvalue())
# print(f.getvalue().decode("utf-8"))
#
#


import os

def search_file(ppath,file,result=[],count=0):
    #获取该目录下的子目录
    file_path = os.path.join(ppath,file)
    if os.path.exists(file_path):
        result.append(file_path)
        print("获取到文件，路径为 %s" %(file_path))
    # 获取该目录下的子目录
    child_path_list = [os.path.join(ppath,dir) for dir in os.listdir(ppath) if os.path.isdir(os.path.join(ppath,dir))]
    # print(child_path_list)
    # if child_path_list == []:
    #     return result
    for ppath in child_path_list:
        search_file(ppath,file,result=result,count=count)
    return result
if __name__ == "__main__":
    ppath = 'F:/elk'
    print(search_file(ppath,'1.txt'))
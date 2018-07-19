#encoding:utf-8
"""
python文本处理

"""
fpath = r'C:\Windows\system.ini'

with open(fpath,'r') as f:
    lines = f.readlines()
    print(lines)
    f.close()

import xlrd,xlwt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time,os

'''
设置单元格样式
'''


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style

def getInfo(file, index=0):
    info = []
    excel = xlrd.open_workbook(file)
    sheet0 = excel.sheet_by_index(index)
    nrows = sheet0.nrows
    # print(nrows)
    for asset in range(1, nrows):
        assert_info = sheet0.row_values(asset)
        info.append(assert_info)
    return info

total = getInfo("total20180504.xlsx")
itom = getInfo("itom.xls")
print(len(total))
print(len(itom))
increased = []
itom_assetNo = [line[0].strip() for line in itom]
total_assetNo = [line[0].strip() for line in total]

# newfile = xlwt.Workbook()
# sheet0 = newfile.add_sheet(u'sheet0',cell_overwrite_ok=True)

for index in range(len(total_assetNo)):
    if total_assetNo[index] not in itom_assetNo:
        with open("increased.txt",'a+',encoding='utf-8') as f:
            f.write(total_assetNo[index]+'\n')
        increased.append(total[index])


print(len(increased))

for index in range(len(itom_assetNo)):
    if itom_assetNo[index] not in total_assetNo:
        with open("extra.txt", 'a+', encoding='utf-8') as f:
            f.write(itom_assetNo[index] + '\n')

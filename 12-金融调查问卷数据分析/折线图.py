import pandas as pd
import numpy as np
import xlrd
from matplotlib import pyplot as plt
from pylab import mpl

# 图形显示中文设置
mpl.rcParams['font.sans-serif'] = ['SimHei']

file_path = '111.xlsx'
# 利用pandas读取
data = pd.read_excel(file_path)
# 数据的信息,看是否有缺失值等
# print(data.info())

# 按照prov_CHN和province字段进行分组
final_data = data[['prov_CHN', 'province']].groupby(['prov_CHN', 'province']).count()
# 创建两个列表分别来存储省的名字和编号
name = []
number = []
for i in final_data.index:
    for j in i:
        # 如果是字符串类型就说明是省名,如果不是就说明是编号
        if type(j) == str:
            name.append(j)
        else:
            number.append(j)

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
x = name
y = number
plt.plot(x, y)
# 设置x的刻度(因为有点省份太长了,需要倾斜才不会重叠)
plt.xticks(rotation=45)
# 设置图片的标题和标签
plt.title('省份编号图')
plt.ylabel('编号')
# 添加网格,透明度为0.4
plt.grid(alpha=0.4)
# 保存图片(一定要在展示之前保存)
plt.savefig('省份编号图.jpg')
# 展示图片
plt.show()

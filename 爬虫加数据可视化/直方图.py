import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import xlrd
from pylab import mpl

# 图形显示中文设置
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 文件路径
file_path = 'lianjia.xls'
# 使用pandas读取lianjia.xls
data = pd.read_excel(file_path)
# 设置显示全部列(字段),pandas只会显示部分列(字段)
pd.set_option('display.max_columns', None)
# print(data.head()) 查看前5条数据
# print(data.info()) 查看数据的信息,看有没有缺失值之类的
# 获取面积这一列(字段)
area_data = data['面积']
# 使用列表存储面积的数值,下面需要把单位去掉(方便制作直方图)
final_data = []
for i in area_data:
    # 如果有-按-分隔为列表(有的面积是范围)
    if (i.find('-') != -1):
        # 取-前面的数据,
        final_data.append(int(i.split('-')[0]))
    else:
        # 如果没有-就直接去掉面积的单位
        i = int(i.replace('㎡', ''))
        # 添加到列表中
        final_data.append(i)

# 计算极差，看大概需要画多少个竖条行
area_range = max(final_data) - min(final_data)
print(area_range)

# 设置图形大小20为宽，8为高，像素（dpi）
plt.figure(figsize=(20, 8), dpi=80)
# 设置组距
d = 30
# 绘图
plt.hist(final_data, range(min(final_data), max(final_data) + d, d))
# 设置x的刻度
plt.xticks(range(min(final_data), max(final_data) + d, d))
# 设置y的刻度
y_list = [500, 1000, 1500, 2000, 2500, 3000]
plt.yticks(y_list)

# 添加标题
plt.title('链家住房面积分布图')
plt.xlabel('面积(㎡)')
plt.ylabel('数量(个)')

# 绘制网格，透明度（alpha）
plt.grid(alpha=0.3)
# 保存
plt.savefig('lianjia.jpg')
plt.show()
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import xlrd
from pylab import mpl

# 图形显示中文设置
mpl.rcParams['font.sans-serif'] = ['SimHei']

file_path = 'lianjia.xls'

data = pd.read_excel(file_path)
# 设置显示全部列(字段)
pd.set_option('display.max_columns', None)
# print(data.head())
# print(data.info())
area_data = data['面积']
final_data = []
for i in area_data:
    if (i.find('-') != -1):
        final_data.append(int(i.split('-')[0]))
    else:
        i = int(i.replace('㎡', ''))
        final_data.append(i)

# 计算极差
area_range = max(final_data) - min(final_data)
print(area_range)

# 设置图形大小
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

# 绘制网格
plt.grid(alpha=0.3)
# 保存
plt.savefig('lianjia.jpg')
plt.show()
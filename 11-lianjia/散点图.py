import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

# 图形显示中文设置
mpl.rcParams['font.sans-serif'] = ['SimHei']

file_path = 'lianjia.xls'

data = pd.read_excel(file_path)
# 设置显示全部列(字段)
pd.set_option('display.max_columns', None)
# print(data.head())
price_data = data['房租']

final_data = []
for i in price_data:
    if (i.find('-') != -1):
        final_data.append(int(i.split('-')[0]))
    else:
        i = int(i.replace('元/月', ''))
        final_data.append(i)

# 将列表随机打乱(random:随机 shuffle:打乱)
random.shuffle(final_data)

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(list(range(len(final_data)))[::5], final_data[::5])
plt.title('链家房租价格分布图')
plt.xlabel('编号')
plt.ylabel('价格(元/月)')
plt.grid(alpha=0.3)
plt.savefig('price_lianjia.jpg')
plt.show()
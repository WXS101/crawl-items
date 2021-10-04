import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

# 图形显示中文设置
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 文件路径
file_path = 'lianjia.xls'
# 利用pandas读取lianjia.xls
data = pd.read_excel(file_path)
# 设置显示全部列(字段)
pd.set_option('display.max_columns', None)
# print(data.head()) 显示前五行
# 获取房租列(字段)
price_data = data['房租']

# 创建一个列表存放房租数值的数据
final_data = []
for i in price_data:
    # 如果有-就按-分隔,并取前面的数据(例如有的数据是4000-5000元/月)
    if (i.find('-') != -1):
        final_data.append(int(i.split('-')[0]))
    else:
        # 其他的就直接去掉元/月方便画图
        i = int(i.replace('元/月', ''))
        final_data.append(i)

# 将列表随机打乱(random:随机 shuffle:打乱),你也可以试一下不打乱
random.shuffle(final_data)

# 设置图片大小20为宽,8为高,dpi(像素)
plt.figure(figsize=(20, 8), dpi=80)
# 每隔五个取一个值,因为值太多了,点就重合了,就不太好看
# 绘制散点图
plt.scatter(list(range(len(final_data)))[::5], final_data[::5])
# 添加标题和标签
plt.title('链家房租价格分布图')
plt.xlabel('编号')
plt.ylabel('价格(元/月)')
# 添加网格并设置透明度alpha
plt.grid(alpha=0.3)
# 保存图片为price_lianjia.jpg
plt.savefig('price_lianjia.jpg')
plt.show()
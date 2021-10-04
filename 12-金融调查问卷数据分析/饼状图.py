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
# 查看后发现我们需要的数据没有缺失值,就不需要对缺失值进行处理

# 按照prov_CHN字段进行分组,并且只取prov_CHN字段,最后计算分组后的数据出现的次数(count)
prov_CHN = data.groupby('prov_CHN')['prov_CHN'].count()
# 最后的值为series类型,把index和values分别存入列表中,方便后面画图
name = list(prov_CHN.index)
sum = prov_CHN.values.tolist()

# 设定图片大小,第一个15为宽,第二个15为长,dpi为像素
plt.figure(figsize=(15, 15), dpi=80)
# 绘制饼状图
plt.pie(sum, labels=name, autopct='%3.2f%%')
# 设置图片的标题
plt.title('调差问卷之调差省份占比率')

# 保存图片(一定要在展示之前保存)
plt.savefig('占比率图.jpg')
# 展示图片
plt.show()

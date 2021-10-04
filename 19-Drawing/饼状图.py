import pandas as pd
from matplotlib import pyplot as plt

# 使用pandas读取文件
df = pd.read_csv(r"news_dataset1.csv")
# 获取内容
x = df['Event'].value_counts().index.tolist()
# 获取内容对应的数据
y = df['Event'].value_counts().tolist()
# 设置显示中文
plt.rcParams['font.sans-serif'] = ['simhei']
# 绘图
plt.pie(x=y, labels=x, autopct='%.2f%%')
# 添加标签,可以给饼状图添加标题
# plt.title("")
# 定义文件名
pie_svg = '饼状图.png'
# 保存图片
plt.show()
# plt.savefig(pie_svg)
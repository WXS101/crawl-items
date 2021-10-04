import pandas as pd
from matplotlib import pyplot as plt

# 读取csv数据
data = pd.read_csv('news_dataset1.csv')
# 取步长4000,不然一百万数据会占满整个画布
hour = data['Date'].str[11:13].tolist()[::4000]
# print(len(hour[::5000]))
new_hour = []
# 转为int,方便后续设置刻度
for i in hour:
    new_hour.append(int(i))
index = range(len(new_hour))
# print(len(index))

# 显示中文不报错,不乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制画布大小长20,宽8,像素80
plt.figure(figsize=(20, 8), dpi=80)
# 图的标题,字体大小20
plt.title('Daily news specific hour distribution map', fontsize=20)
# x轴的标签,编号0开始就是第一个数据,字体大小20
plt.xlabel('number', fontsize=20)
# y轴的标签,字体大小20
plt.ylabel('time', fontsize=20)
# 设置y轴的刻度
plt.yticks([0, 5, 10, 15, 20], ['0:00', '5:00', '10:00', '15:00', '20:00'])
# 设置网格
plt.grid(alpha=0.4)
# 设置刻度字体大小,字体大小20
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 绘制散点图
plt.scatter(index, new_hour)
plt.savefig('Daily news specific hour distribution map.png')
plt.show()
'''
最后可以看出来,几乎每个小时的新闻数量都差不多,新闻数量比较规律
'''

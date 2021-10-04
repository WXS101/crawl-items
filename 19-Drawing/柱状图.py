import pandas as pd
from matplotlib import pyplot as plt

# 设置显示中文
plt.rcParams['font.sans-serif'] = ['simhei']
# 使用pandas读取文件
df = pd.read_csv(r"news_dataset1.csv")
# 获取x轴数据
x = df['Date'].str[:10].value_counts().index.tolist()
# 获取y轴数据
y = df['Date'].str[:10].value_counts().tolist()
# 定义画布
fig = plt.figure(figsize=(20, 10))
# 绘制柱状图
plt.bar(x, y, tick_label=x)
# 让x轴旋转90度,方便观看
plt.xticks(x, x, rotation=90)
# 添加标签
plt.xlabel("date")
plt.ylabel("the frequency of appearance")
plt.title("The frequency of the date")
# 保存图片
plt.savefig("柱状图.png")

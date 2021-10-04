import xlrd
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba


def wordcloud(text):
    # 分词
    cut = jieba.cut(text)
    string = " ".join(cut)
    # 打开遮罩图片
    img = Image.open(r"prcie.jpg")
    # 将图片转换为数组
    img_array = np.array(img)
    # 设置参数
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path="msyh.ttc"
    )
    wc.generate_from_text(string)
    fig = plt.figure(1)
    plt.imshow(wc)
    # 是否显示坐标轴
    plt.axis('off')
    # 显示生成的词云图片,可以直接保存就注释了
    # plt.show()
    # 保存
    plt.savefig(r'wordcloud.jpg', dpi=500)

data_list = []
wb = xlrd.open_workbook("lianjia.xls")
sh = wb.sheet_by_name('Sheet')
for i in range(1, 10201):
    data_list.append(sh.cell(i, 0).value)
text = "".join(data_list)
wordcloud(text)
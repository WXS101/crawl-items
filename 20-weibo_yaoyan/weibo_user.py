import json
import xlrd
import requests
import time
from lxml import etree
from openpyxl import Workbook
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter
import pandas as pd


def get_data(url):
    # 定义请求头
    head = {
        "MWeibo-Pwa": "1",
        "Referer": "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3DHM",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    }
    # 获取响应
    response = requests.get(url, headers=head)
    # 转换为json
    response = response.json()
    # 拿到cards里面的数据
    data = response['data']['cards']
    # print(data)
    # 遍历
    for j in range(len(data)):
        # 防止报错
        try:
            # 拿到text里面的数据
            # thumbs 是点赞数
            thumbs = data[j]["mblog"]["comments_count"]
            # forward 是转发数
            forward = data[j]["mblog"]['reposts_count']
            # 用户名
            user_name = data[j]["mblog"]["user"]["screen_name"]
            # 是否被认证
            authen = data[j]["mblog"]["user"]['verified']
            # 判断
            if authen == "TRUE":
                authen_res = "是"
            else:
                authen_res = "否"
            # 获取text标签的数据,来得到内容
            result = data[j]['mblog']['text']
            # 使用xpath获取具体的数据
            res = etree.HTML(result)
            # 处理数据
            a = "".join(res.xpath('//text()'))
            # 判断 # 是否在内容里面
            if "#" in a:
                address = "是"
            else:
                address = "否"
            # 添加到datalist列表里面
            data_list.append([user_name, authen_res, thumbs, forward, address, a])
        except KeyError as p:
            continue
    # 打印一下,查看进度,也可以不打印
    print(data_list)


if __name__ == '__main__':
    # 定义一个列表,存储数据
    data_list = []
    # 循环爬取,这里是循环200页
    for i in range(200):
        try:
            # 停一秒,防止被封ip
            time.sleep(1)
            # 爬取的网址
            # 下面的url 和 url_2 等等是不同话题下的接口,想用谁就传入谁作为参数
            url_2 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%E7%83%AD%E7%82%B9%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page="+str(i)+""
            url = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page="+str(i)+""
            url_3 = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E7%A4%BE%E4%BC%9A&page_type=searchall&page=" + str(
                i) + ""
            url_4 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%E4%B8%87%E8%B1%A1%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page=" + str(
                i) + ""
            url_5 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%E7%A7%91%E5%AD%A6%23&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page=" + str(
                i) + ""
            url_6 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89%E6%A0%B8%E5%BF%83%E4%BB%B7%E5%80%BC%E8%A7%82%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page=" + str(
                i) + ""
            url_7 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E8%B7%B5%E8%A1%8C%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89%E6%A0%B8%E5%BF%83%E4%BB%B7%E5%80%BC%E8%A7%82%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page=" + str(
                i) + ""
            url_8 = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A4%BE%E4%BC%9A%E5%B7%A5%E4%BD%9C%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E7%A4%BE%E4%BC%9A%26t%3D0&page_type=searchall&page=" + str(
                i) + ""
            # 打印一下网址,查看进度,也可以不打印
            print(url_8)
            # 调用函数
            get_data(url_8)
        except:
            continue

    # 使用Workbook保存数据到 微博_谣言.xlsx文件中, 换了url的话,也要换文件名,不然要被替代
    fire = Workbook()
    sheet = fire.active
    sheet.append(["用户名", "用户是否被认证", "点赞数", "转发数", "文本是否包含url地址符", "内容"])
    for m in data_list:
        sheet.append(m)
    fire.save('微博_社会1.xlsx')

    # 使用pandas库去重
    data = pd.read_excel("微博_社会.xlsx")
    data = pd.DataFrame(data)
    data.drop_duplicates(subset=["用户名"], keep='first', inplace=True)
    data.to_excel("微博_社会.xlsx", index=False)

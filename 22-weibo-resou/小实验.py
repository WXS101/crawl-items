# -*- coding: utf-8 -*-
import json
import xlrd
import re
from fake_useragent import UserAgent
import requests
import asyncio
from matplotlib.font_manager import FontProperties
import sched
import aiohttp
import time
from lxml import etree
from openpyxl import Workbook
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pymongo
import os


# 保存热搜话题下的数据的函数,保存到xlsx文件中
def sava_resou_data(data_list, i, resou_title):
    fire = Workbook()
    sheet = fire.active
    sheet.append(["time", "content"])
    for m in data_list:
        sheet.append(m)
    fire.save(resou_title[i] + '.xls')


# 保存自定义话题下的数据,保存到xlsx文件中
def sava_zidingyi_data(data_list, name):
    fire = Workbook()
    sheet = fire.active
    sheet.append(["time", "content"])
    for m in data_list:
        sheet.append(m)
    fire.save(name + '.xls')


async def get_data(data_list, html):
    # 把数据转换为json格式
    response = json.loads(html)
    # 拿到cards标签下的数据
    data = response['data']['cards']
    for j in range(len(data)):
        try:
            # 拿到created_at标签下的数据,也就是时间
            res_time = data[j]['mblog']['created_at']
            res = res_time.split()
            # 对日期进行处理,转换为正常的日期格式
            temp = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
            a = lambda x: (temp[x - 1], f"0{x}") if x < 10 else (temp[x - 1], f"{x}")
            month_dict = dict([a(i) for i in range(1, 13)])
            fin_time = res[-1] + "-" + month_dict[res[1]] + "-" + res[2] + " " + res[3]
            # 拿到text标签下的数据,再用xpath拿到所有的文本内容
            result = data[j]['mblog']['text']
            res = etree.HTML(result)
            fin_text = "".join(res.xpath('//text()'))
            # 把数据添加到data_list数组中去
            data_list.append([fin_time, fin_text])
            # 显示一下数据
            print(fin_time, fin_text)
        except KeyError as p:
            pass
    # print(len(data_list))
    # print(data_list)


def change_ip(proxies_url):
    # 更换ip
    while True:
        try:
            proxies = "http://" + requests.get(proxies_url).text.split("\r\n")[0]
            break
        except Exception as p:
            time.sleep(2)
            print("请求ip出错")
    return proxies


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def get_resou_url(url, proxies_url):
    # 定义请求头
    head = {
        "User-Agent": UserAgent().random
    }
    # 获取响应
    response = requests.get(url, headers=head)
    # 转换为json
    response = response.json()
    # 拿到cards里面的数据
    data = response['data']['cards'][0]['card_group']
    # 拿到热搜中前10个的标题
    for res in range(10):
        resou_title.append(data[res]['desc'])
    print(resou_title)

    # print(data)
    while True:
        try:
            proxies = "http://" + requests.get(proxies_url).text.split("\r\n")[0]
            break
        except Exception as p:
            time.sleep(2)
            print("请求ip出错")
    # 遍历
    for j in range(10):
        # 拿到text里面的数据
        scheme = data[j]['scheme'].split("?")
        data_list = []
        i = "0"
        new_urls = [
            "https://m.weibo.cn/api/container/getIndex?" + scheme[1] + "&page_type=searchall&page=" + str(i) + "" for i
            in range(1, 200)]
        for url_one in new_urls:
            try:
                # 使用协程爬取,加快效率
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:
                    # 显示网址,可以查看进度
                    print(url_one)

                    async with session.get(url_one, headers=head,
                                           proxy=proxies, timeout=15) as response:
                        html = await response.text()
                        # 判断一个话题下的数据是否爬取完,如果爬取完,就跳出循环
                        a = re.findall('"ok":(.*?),"data"', html, re.S)
                        if "msg" in a[0]:
                            break
                        await get_data(data_list, html)
            except Exception as p:
                print(p)
                proxies = change_ip(
                    "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4")
                continue
        # 调用保存数据到xlsx文件中的函数
        sava_resou_data(data_list, j, resou_title)
    return resou_title


async def get_zidingyi_url(url, name, proxies_url):
    # 定义请求头
    head = {
        "User-Agent": UserAgent().random
    }
    while True:
        try:
            proxies = "http://" + requests.get(proxies_url).text.split("\r\n")[0]
            break
        except Exception as p:
            time.sleep(2)
            print("请求ip出错")
    data_list = []
    # 处理url变成接口
    scheme = url.split("?")
    i = "0"
    new_urls = [
        "https://m.weibo.cn/api/container/getIndex?" + scheme[1] + "&page_type=searchall&page=" + str(i) + "" for i
        in range(1, 200)]
    for url_one in new_urls:
        try:
            # 使用协程加快效率
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:
                # 显示网址,可以查看进度
                print(url_one)

                async with session.get(url_one, headers=head,
                                       proxy=proxies, timeout=15) as response:
                    html = await response.text()
                    # 判断话题下的数据是否爬取完,如果爬取完,就跳出循环
                    a = re.findall('"ok":(.*?),"data"', html, re.S)
                    if "msg" in a[0]:
                        break
                    await get_data(data_list, html)
        except Exception as p:
            print(p)
            proxies = change_ip(
                "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4")
            continue
    # 调用保存数据到xlsx文件中的函数
    sava_zidingyi_data(data_list, name)


def histogram(resou_title, user_input):
    # 制作柱状图
    chart_list = []
    name_list = []
    # 从保存的xlsx文件中拿到数据,然后判断词条数
    for i in range(10):
        df = pd.read_excel(resou_title[i] + ".xls")
        res = "".join(df["content"].values)
        num = int(res.count("#") / 2)
        chart_list.append(num)
        name_list.append(resou_title[i])
    # 从保存的xlsx文件中拿到数据,然后判断词条数
    for i in range(5):
        df = pd.read_excel(user_input[i] + ".xls")
        res = "".join(df["content"].values)
        num = int(res.count("#") / 2)
        chart_list.append(num)
        name_list.append(user_input[i])
    # 设置图片可以显示中文和负数
    # plt.rcParams['font.sans-serif'] = ['simhei']
    plt.rcParams['axes.unicode_minus'] = False

    # x轴
    x = np.array(name_list)
    # y轴
    y = np.array(chart_list)
    # 倒序，返回排序后各数据的原始下标
    sortIndex = np.argsort(-y)
    # 重新进行排序，与y保持初始顺序一致
    x_sort = x[sortIndex]
    # 重新进行排序，倒序
    y_sort = y[sortIndex]

    def autolabel(rects, font):
        # 显示词条数
        for rect in rects:
            height = rect.get_height()

            plt.text(rect.get_x() + rect.get_width() / 2. - 0.25, 1.01 * height, '%s' % int(height),
                     fontproperties=font)

    font = FontProperties(fname=r"./simhei.ttf")
    # 让x轴的标题旋转90度,方便显示
    plt.xticks(np.arange(len(x_sort)), x_sort, rotation=90, fontproperties=font)
    # 作图
    a = plt.bar(np.arange(len(x_sort)), y_sort)
    # 调用显示词条数的函数
    autolabel(a, font)
    # 设置标题
    plt.title('词条数统计', fontproperties=font)
    # 设置y轴的单位
    plt.ylabel('词条数', fontproperties=font)
    # 设置x轴的单位
    plt.xlabel('词条', fontproperties=font)
    # 保存图片
    plt.savefig("15.jpg")


def line_chart(resou_title, user_input):
    # 制作折线图
    # 设置可以在图片上显示中文和负数
    # plt.rcParams['font.sans-serif'] = ['simhei']
    plt.rcParams['axes.unicode_minus'] = False
    # 遍历10个热搜的文件作图
    for i in range(10):
        df = pd.read_excel(resou_title[i] + ".xls")
        x_time = df["time"].str[:10].value_counts().index.tolist()
        y_time = df["time"].str[:10].value_counts().tolist()
        # 设置画布
        plt.figure(figsize=(20, 8), dpi=80)
        # x轴的标题旋转90度
        plt.xticks(rotation=90)
        # 作图
        plt.plot(x_time, y_time)

        font = FontProperties(fname=r"./simhei.ttf")

        # 定义x轴的标题
        plt.xlabel("发布时间", fontproperties=font)
        # 定义y轴的标题
        plt.ylabel("时间频率", fontproperties=font)
        # 定义整个图片的标题
        plt.title(resou_title[i] + "发布时间和时间频率对应关系图", fontproperties=font)
        # 保存图片
        plt.savefig("" + str(i) + ".jpg")

    for i in range(5):
        df = pd.read_excel(user_input[i] + ".xls")
        x_time = df["time"].str[:10].value_counts().index.tolist()
        y_time = df["time"].str[:10].value_counts().tolist()
        # 设置画布
        plt.figure(figsize=(20, 8), dpi=80)
        # 让x轴的数据旋转90度,方便显示
        plt.xticks(rotation=90)
        # 作图
        plt.plot(x_time, y_time)

        font = FontProperties(fname=r"./simhei.ttf")

        # 定义x轴的标题
        plt.xlabel("发布时间", fontproperties=font)
        # 定义y轴的标题
        plt.ylabel("时间频率", fontproperties=font)
        # 定义整个图片的标题
        plt.title(user_input[i] + "发布时间和时间频率对应关系图", fontproperties=font)
        # 保存图片
        plt.savefig("" + str(i + 10) + ".jpg")


def main():
    mongo_py = pymongo.MongoClient()

    collection = mongo_py['weibo_citiao']['data']
    resou_title = []
    # 类似于这种 user_input = ["美食", "美味", "熊猫", "动物", ""]
    user_input = ["美食", "美味", "熊猫", "动物", "狗"]
    url = "https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=seat%3D1%26pos%3D0_0%26dgr%3D0%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time%3D1620121386&luicode=10000011&lfid=231583"
    # ip网址
    proxies_url = "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"

    # loop = asyncio.get_event_loop()
    # task = [asyncio.ensure_future(get_resou_url(url, proxies_url))]
    # loop.run_until_complete(asyncio.wait(task))
    # 使用协程调用函数
    asyncio.run(get_resou_url(url, proxies_url))

    # 自定义的五个网址
    urls = ["https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D" + user_input[0],
            "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D" + user_input[1],
            "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D" + user_input[2],
            "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D" + user_input[3],
            "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D" + user_input[4]]
    # 调用函数

    for i in range(5):
        asyncio.run(get_zidingyi_url(urls[i], user_input[i], proxies_url))
    # 调用柱状图函数
    histogram(resou_title, user_input)
    # 调用折线图函数
    line_chart(resou_title, user_input)

    try:
        for m in range(10):
            collection.update_one({'id': m}, {'$set': {'name': resou_title[m]}})
            os.remove(resou_title[m] + '.xls')

        for j in range(10, 15):
            collection.update_one({'id': j}, {'$set': {'name': user_input[j - 10]}})
            os.remove(user_input[j - 10] + '.xls')
    except Exception as p:
        print(p)


def timedTask(res_time, user_input):
    # 初始化 sched 模块的 scheduler 类
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务
    scheduler.enter(res_time, 1, main, argument=(user_input,))
    # 运行任务
    scheduler.run()


if __name__ == '__main__':
    # mongo_py = pymongo.MongoClient()
    #
    # collection = mongo_py['weibo_citiao']['data']
    # resou_title = []
    # # 类似于这种 user_input = ["美食", "美味", "熊猫", "动物", ""]
    # user_input = ["美食", "美味", "熊猫", "动物", "狗"]
    # start_time = time.time()
    main()
    # 把标题存入数据库和删除生成的xlsx文件,避免服务器压力过大
    # try:
    #     for m in range(10):
    #         collection.update_one({'id': m}, {'$set': {'name': resou_title[m]}})
    #         os.remove(resou_title[m]+'.xls')
    #
    #     for j in range(10, 15):
    #         collection.update_one({'id': j}, {'$set': {'name': user_input[j-10]}})
    #         os.remove(user_input[j-10] + '.xls')
    # except Exception as p:
    #     print(p)
    #
    # end_time = time.time()
    # 计算时间,一个小时跑一次
    # 无限循环
    # while True:
    #     resou_title = []
    #     start_time = time.time()
    #     timedTask(res_time, user_input)
    #
    #     try:
    #         for m in range(10):
    #             collection.update_one({'id': m}, {'$set': {'name': resou_title[m]}})
    #             os.remove(resou_title[m] + '.xls')
    #
    #         for j in range(10, 15):
    #             collection.update_one({'id': j}, {'$set': {'name': user_input[j - 10]}})
    #             os.remove(user_input[j - 10] + '.xls')
    #     except Exception as p:
    #         print(p)
    #
    #     end_time = time.time()
    #     fin_time = end_time - start_time
    #     res_time = 3600 - int(fin_time)
    #     if res_time <= 0:
    #         res_time = 10
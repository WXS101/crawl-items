import requests
from lxml import etree
import pymongo
import pandas as pd
import time
from openpyxl import Workbook
import threading

data_list = []

mongo_py = pymongo.MongoClient()

collection = mongo_py['lianjia_nb_two']['data']


def get_response(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def get_all_url(response):
    url_list = []
    response = etree.HTML(response)
    urls = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/@href')
    for url in urls:
        url_list.append(url)
    return url_list


def parse_data(fin_url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    fin_response = requests.get(fin_url, headers=head).text
    response = etree.HTML(fin_response)
    name_residential = response.xpath('//*[@class="content"]/div[4]/div[1]/a[1]/text()')[0]
    address = "".join(response.xpath('/html/body/div[5]/div[2]/div[4]/div[2]/span[2]//text()')).split('\xa0')
    address = address[0] + " " + address[1]
    type_house = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()')[0]
    area = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()')[0]
    orientation = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()')[0]
    renovation = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()')[0]
    floor_distribution = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()')[0]
    elevator = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()')[0]
    price = response.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/span//text()')
    price = price[0] + price[1]
    time_listing = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()')[0]
    time_transaction = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()')[0]
    data_list.append(
        [name_residential, address, type_house, area, orientation, renovation, floor_distribution, elevator, price,
         time_listing, time_transaction])


def multi_thread(urls):
    threads = []
    for url in urls:
        try:
            print(url)
            threads.append(threading.Thread(target=parse_data, args=(url,)))
        except IndexError:
            continue
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main():
    for i in range(1, 101):
        print(i)
        # 因为网站有限制,所以要根据筛选条件来爬取
        # 海曙区
        url1 = "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a1a6a7a8/"
        url2 = "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a2/"
        url3 = "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a3/"
        url4 = "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a4/"
        url5 = "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a5/"
        # 镇海区
        url6 = "https://nb.lianjia.com/ershoufang/zhenhaiqu1/pg" + str(i) + "p7p8/"
        url7 = "https://nb.lianjia.com/ershoufang/zhenhaiqu1/pg" + str(i) + "p1p2p3p4p5p6/"
        # 北仑区
        url8 = "https://nb.lianjia.com/ershoufang/beilunqu1/pg" + str(i) + "p7p8/"
        url9 = "https://nb.lianjia.com/ershoufang/beilunqu1/pg" + str(i) + "p1p2p3p4p5p6/"
        # 江北区
        url10 = "https://nb.lianjia.com/ershoufang/jiangbeiqu1/pg" + str(i) + "l1l2l4l5/"
        url11 = "https://nb.lianjia.com/ershoufang/jiangbeiqu1/pg" + str(i) + "l3l6/"
        # 鄞州区
        url12 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp0ep70/"
        url13 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp70ep140/"
        url14 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp140ep230/"
        url15 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp230ep290/"
        url16 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp290ep350/"
        url17 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp350ep440/"
        url18 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp440ep520/"
        url19 = "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp520ep10000/"
        # 所有的url
        urls = ["https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a1a6a7a8/",
                "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a2/",
                "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a3/",
                "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a4/",
                "https://nb.lianjia.com/ershoufang/haishuqu1/pg" + str(i) + "a5/",
                "https://nb.lianjia.com/ershoufang/zhenhaiqu1/pg" + str(i) + "p7p8/",
                "https://nb.lianjia.com/ershoufang/zhenhaiqu1/pg" + str(i) + "p1p2p3p4p5p6/",
                "https://nb.lianjia.com/ershoufang/beilunqu1/pg" + str(i) + "p7p8/",
                "https://nb.lianjia.com/ershoufang/beilunqu1/pg" + str(i) + "p1p2p3p4p5p6/",
                "https://nb.lianjia.com/ershoufang/jiangbeiqu1/pg" + str(i) + "l1l2l4l5/",
                "https://nb.lianjia.com/ershoufang/jiangbeiqu1/pg" + str(i) + "l3l6/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp0ep70/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp70ep140/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp140ep230/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp230ep290/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp290ep350/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp350ep440/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp440ep520/",
                "https://nb.lianjia.com/ershoufang/yinzhouqu2/pg" + str(i) + "bp520ep10000/"]
        time.sleep(0.5)
        # 把所有的url运行一遍
        for url in urls:
            response = get_response(url)
            url_list = get_all_url(response)

            multi_thread(url_list)

    # 把数据保存到mongodb数据库
    for j in range(len(data_list)):
        collection.insert_one({
            "小区名称": data_list[j][0],
            "所处行政区域": data_list[j][1],
            "户型": data_list[j][2],
            "面积": data_list[j][3],
            "朝向": data_list[j][4],
            "装修": data_list[j][5],
            "楼层分布": data_list[j][6],
            "有无电梯": data_list[j][7],
            "房屋单价": data_list[j][8],
            "挂牌时间": data_list[j][9],
            "交易时间": data_list[j][10],
        })

    # 把数据保存到excel里面
    fin_data_list = []
    for item in collection.find():
        fin_data_list.append(
            [item['小区名称'], item['所处行政区域'], item['户型'], item['面积'], item['朝向'], item['装修'], item['楼层分布'], item['有无电梯'],
             item['房屋单价'], item["挂牌时间"], item["交易时间"]])
    fire = Workbook()
    sheet = fire.active
    sheet.append(['小区名称', '所处行政区域', '户型', '面积', '朝向', '装修', '楼层分布', '有无电梯', '房屋单价', '挂牌时间', '交易时间'])
    for i in fin_data_list:
        sheet.append(i)
    fire.save('lianjia_nb_two.xlsx')


if __name__ == '__main__':
    main()

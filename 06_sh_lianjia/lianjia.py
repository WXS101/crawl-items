import requests
from lxml import etree
import pymongo
from selenium import webdriver
import time
from openpyxl import Workbook

data_list = []

mongo_py = pymongo.MongoClient()

collection = mongo_py['lianjia_sh']['data']


def get_response(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    response = etree.HTML(response)
    datas = response.xpath('//*[@id="content"]/div[1]/div[1]/div')
    for data in datas:
        title = data.xpath('./div/p[1]/a/text()')[0].replace(" ", "").replace("\n", "")
        price_one = data.xpath('./div/span/em/text()')[0]
        price_two = data.xpath('./div/span/text()')[0]
        price = (price_one + price_two).replace(" ", "")
        for i in range(1, 8):
            area = data.xpath('./div/p[2]/text()[' + str(i) + ']')
            if area == []:
                continue
            else:
                area = area[0].replace(" ", "")
                if "㎡" in area:
                    break
                else:
                    continue
        area = area.replace("\n", "")
        for i in range(1, 8):
            house = data.xpath('./div/p[2]/text()[' + str(i) + ']')
            if house == []:
                continue
            else:
                house = house[0].replace(" ", "")
                if "室" in house:
                    break
                else:
                    continue
        house = house.replace("\n", "")
        img_url = data.xpath('./a/img/@data-src')[0]
        data_list.append([title, price, area, house, img_url])


def main():
    for i in range(1, 101):
        print(i)
        # 因为网站有限制,所以要爬4个网站
        url1 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp1rp2rp3rp4"
        url2 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp5"
        url3 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp6"
        url4 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp7"
        time.sleep(2)
        response = get_response(url4)
        parse_data(response)
    print(data_list)

    # 把数据保存到mongodb数据库
    for i in range(len(data_list)):
        collection.insert_one({
            "简介": data_list[i][0],
            "房租": data_list[i][1],
            "面积": data_list[i][2],
            "户型": data_list[i][3],
            "img_url": data_list[i][4]
        })

    # 把数据保存到excel里面
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["简介", "房租", "面积", "户型", "img_url"])
    for i in data_list:
        sheet.append(i)
    workbook.save('lianjia.xls')


if __name__ == '__main__':
    # main()
    options = webdriver.ChromeOptions()
    wb = webdriver.Chrome(r"E:\python3.8.3\Scripts\chromedriver.exe", options=options)
    wb.get("img.html")

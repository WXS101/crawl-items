import requests
from lxml import etree
import pymongo
import time
from openpyxl import Workbook

# 定义一个列表来存储下面要获取的数据
data_list = []
# 连接mongodb需要用到的
mongo_py = pymongo.MongoClient()

collection = mongo_py['lianjia_sh']['data']

# 获取响应的方法(需要传入地址参数)
def get_response(url):
    # 请求头添加user-agent，模仿浏览器（让服务器不知道这是爬虫程序，以为是浏览器）
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    # requests的get方法获取url的响应
    response = requests.get(url, headers=head)
    # 响应码为200就返回网页源代码（response.text）
    if response.status_code == 200:
        return response.text
    else:
        # 否则就返回访问错误
        print("访问网页错误")

# 解析响应的内容,获取自己想要获取的内容(传入响应的参数)
def parse_data(response):
    # 利用lxml库的etree模块解析网页的结构,生成xpath可以解析的对象
    response = etree.HTML(response)
    # 使用xpath解析网页
    datas = response.xpath('//*[@id="content"]/div[1]/div[1]/div')
    for data in datas:
        # 获取自己想要的数据
        # 简介
        title = data.xpath('./div/p[1]/a/text()')[0].replace(" ", "").replace("\n", "")
        # 月租的具体的数值(比如2400)
        price_one = data.xpath('./div/span/em/text()')[0]
        # 月租的单位(比如元/每月)
        # 把月租的具体的数值和单位分开,防止数据发生不必要的错误
        price_two = data.xpath('./div/span/text()')[0]
        # 合并月租的具体数值和单位
        price = (price_one + price_two).replace(" ", "")
        # 循环七次,因为下面的xpath包含七个值(我们只需要获取我们想要的值即可)
        for i in range(1, 8):
            # 获取area(面积)的值(因为有些面积数据为空,所以下面要对面积的只进行判断)
            area = data.xpath('./div/p[2]/text()[' + str(i) + ']')
            # 如果为空(有些网页上也没有数据),继续循环
            if area == []:
                continue
            else:
                # 如果不为空,就先替换空格,
                area = area[0].replace(" ", "")
                # 如果㎡在里面,就说明找到了我们想要的数据,就退出循环
                if "㎡" in area:
                    break
                # 否则就继续
                else:
                    continue
        # 换行去掉(有些数据)
        area = area.replace("\n", "")
        # house:(房屋户型)这个数据和面积数据一样(也是在七个数据之间的一个数据,做法和面积一样)
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
        # 通过xpath获取图片
        img_url = data.xpath('./a/img/@data-src')[0]
        # 最后把各个数据(字段)添加到data_list列表中
        data_list.append([title, price, area, house, img_url])


def main():
    # 循环100次,链家只能爬取到第100页
    for i in range(1, 101):
        print(i)
        # 因为网站有限制,所以要爬4个页面(有点数据需要点进去(点击图片或者点击文字)才能爬取)
        url1 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp1rp2rp3rp4"
        url2 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp5"
        url3 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp6"
        url4 = "https://sh.lianjia.com/zufang/pg"+str(i)+"rp7"
        # 每循环一次,等两秒再进行下一次循环,防止网页封ip
        time.sleep(2)
        # 传入地址参数
        response = get_response(url4)
        # 解析获取的响应
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
    # 先把字段名添加到最开头
    sheet.append(["简介", "房租", "面积", "户型", "img_url"])
    # 把data_list的数据添加到xls中
    for i in data_list:
        sheet.append(i)
    # 保存到xls文件中,文件名为lianjia
    workbook.save('lianjia.xls')


if __name__ == '__main__':
    main()

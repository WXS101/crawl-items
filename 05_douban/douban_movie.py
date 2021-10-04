import requests
from lxml import etree
from openpyxl import Workbook

data_list = []


def get_response(url):
    # 设置header
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    # 用requests函数获取响应
    response = requests.get(url, headers=head)
    # 如果响应码为200,代表成功,返回内容,如果不成功,则打印"访问网页错误"
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    data = etree.HTML(response)
    # 用xpath解析得到数据
    names = data.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    # 循环加入列表
    for name in names:
        data_list.append(name)


def main():
    # 设置爬取几页
    for i in range(4):
        i = str(i)
        # 获取要爬取的网页
        url = "https://movie.douban.com/top250?start=" + i + "&filter="
        # 获取响应的内容
        response = get_response(url)
        # 获取数据
        parse_data(response)
    # 把数据保存到xlsx文件中
    file = Workbook()
    sheet = file.active
    # 设置标题
    sheet.append(["排名", "排行榜"])
    for i in range(100):
        # i+1代表排名,循环保存数据
        sheet.append([i+1, data_list[i]])
    file.save('豆瓣.xlsx')


if __name__ == '__main__':
    main()

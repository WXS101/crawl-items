# 导入包
import requests
from lxml import etree
import random
import time
import os


def get_response(url):
    # 获取网页的响应
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    response = requests.get(url, headers=head)
    # 如果响应码为200,获取成功,返回内容,如果不是200,则打印访问网页错误
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response, path):
    # 用xpath解析数据
    html = etree.HTML(response)
    # 这是创建所有的文件夹
    file_names = ("Archean Cratons","Complex Volcanic Settings","Continental Flood Basalts","Convergent Margins","Inclusions","Intraplate Volcanics","Minerals","Oceanic Plateaus","Ocean Basin Flood Basalts","Ocean Island Groups   Single Islands","Rift Volcanics","Rocks","Seamounts","Submarine Ridges")

    # 遍历创建文件夹
    for file_name in file_names:
        isExists = os.path.exists(path + file_name)
        if not isExists:
            os.makedirs(path + file_name)

    # 用for循环遍历所有的文件
    for i in range(3, 31):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Archean Cratons\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(33, 40):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Complex Volcanic Settings\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(42, 84):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Continental Flood Basalts\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(84, 131):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Convergent Margins\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(133, 134):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Inclusions\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(136, 271):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        print(data)
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Intraplate Volcanics\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(273, 292):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Minerals\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(294, 312):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Oceanic Plateaus\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(314, 320):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Ocean Basin Flood Basalts\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(322, 371):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Ocean Island Groups   Single Islands\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(373, 393):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Rift Volcanics\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(395, 463):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Rocks\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(465, 562):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Seamounts\\"+name, "wb") as f:
            f.write(result.content)

    # 用for循环遍历所有的文件
    for i in range(564, 591):
        data = html.xpath('//*[@id="tcompfiles"]/tr[' + str(i) + ']/td[1]/a/@href')[0]
        # 获取文件的url
        down_url = "http://georoc.mpch-mainz.gwdg.de/" + data
        # 打印i查看进度
        print(i)
        # 找出文件名
        name = data.split("/", 4)[-1]
        # 保存文件,按顺序保存
        result = requests.get(down_url)
        with open(".\\Submarine Ridges\\"+name, "wb") as f:
            f.write(result.content)


def main():
    # 随机延时,可以不用
    # time.sleep(random.uniform(1, 4))
    # 网址需要进一步查找,这就不用修改了
    url = "http://georoc.mpch-mainz.gwdg.de/GEOROC/CompFiles.aspx"
    # 调用函数
    response = get_response(url)
    # 这里需要设置成这个py文件的上一层目录
    path = r'E:\pycharm\work\13-download_csv/'
    parse_data(response, path)


if __name__ == '__main__':
    main()
import requests
import time
from lxml import etree
from openpyxl import Workbook


def get_data(url):
    # 定义请求头
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
    }
    # 获取响应
    response = requests.get(url)
    print(response.text)
    # 转换为json
    response = response.json()
    # 拿到cards里面的数据
    data = response['data']['cards']
    # 遍历
    for j in range(len(data)):
        # 防止报错
        try:
            # 拿到text里面的数据
            result = data[j]['mblog']['text']
            # 使用xpath获取具体的数据
            res = etree.HTML(result)
            # 处理数据
            a = "".join(res.xpath('//text()'))
            if "谣言" in a:
                # 添加到datalist列表里面
                data_list.append([a])
            else:
                continue
        except KeyError as p:
            print("错误")
            continue
    # 打印一下,查看进度,也可以不打印
    print(data_list)


if __name__ == '__main__':
    # 定义一个列表,存储数据
    data_list = []
    # 循环爬取,这里是循环155页
    for i in range(1, 201):
        try:
            # 停一秒,防止被封ip
            time.sleep(1)
            # 爬取的网址
            # url是中国互联网联合辟谣平台的接口
            url = "https://m.weibo.cn/api/container/getIndex?containerid=2304136525943125_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2302836525943125&page_type=03&page="+str(i)+""
            # url_1是微博辟谣的接口
            url_1 = "https://m.weibo.cn/api/container/getIndex?containerid=2304131866405545_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2302831866405545&page_type=03&page="+str(i)+""
            # 打印一下网址,查看进度,也可以不打印,这个可改成什么的url或者url_1
            print(url_1)
            # 调用函数,一样可改
            get_data(url_1)
        except:
            continue

    # 使用Workbook保存数据到 微博_谣言.xlsx文件中,改了建议换一个文件名,不然数据会被替代
    fire = Workbook()
    sheet = fire.active
    sheet.append(["content"])
    for m in data_list:
        sheet.append(m)
    fire.save('微博_谣言3.xlsx')

import requests
from openpyxl import Workbook
from lxml import etree
import pymongo
import time
import re

mongo_py = pymongo.MongoClient()

collection = mongo_py['lagou_people']['data']

data_list = []


def get_response(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    data = etree.HTML(response)
    url_list = []
    for i in range(1, 17):
        url = data.xpath('//*[@id="company_list"]/ul/li[' + str(i) + ']/div[1]/h3/a/@href')[0]
        url_list.append(url)
    return url_list


def parse_detail_data(response):
    data = etree.HTML(response)
    people_name = data.xpath('//*[@id="company_managers"]/div[2]/div/ul/li/p[1]/span/text()')
    people_name = "" if people_name == [] else people_name[0]
    if people_name != "":
        people_weibo = "https://s.weibo.com/weibo?q=" + people_name + "&wvr=6&b=1&Refer=SWeibo_box"
    else:
        people_weibo = ""
    people_post = data.xpath('//*[@id="company_managers"]/div[2]/div/ul/li/p[2]/text()')
    people_post = "" if people_post == [] else people_post[0]
    company_url = re.findall(r'"producturl":(.*?),"productprofile"', response)
    company_url = "" if company_url == [] else company_url[0]
    print(people_name, people_post, people_weibo, company_url)
    data_list.append([people_name, people_post, people_weibo, company_url])


def main():
    # 随机延时
    # time.sleep(random.uniform(1, 4))
    # 代填入网址
    # url = "https://www.lagou.com/gongsi/0-0-43-0?isShowMoreIndustryField=true&sortField=1#filterBox"
    # response = get_response(url)
    # urls = parse_data(response)
    # for url_ in urls:
    #     time.sleep(3)
    #     print(url_)
    #     response_ = get_response(url_)
    #     parse_detail_data(response_)
    # fire = Workbook()
    # sheet = fire.active
    # sheet.append(['公司联系人', '公司联系人职称', '公司联系人微博link', '公司官网'])
    # for i in data_list:
    #     sheet.append(i)
    # fire.save('lagou_people.xlsx')
    response = get_response("https://www.lagou.com/gongsi/v1/878c46e36f8e7e67ba190e31720a82226aae7515d571b04f.html")
    parse_detail_data(response)
    fire = Workbook()
    sheet = fire.active
    sheet.append(['公司联系人', '公司联系人职称', '公司联系人微博link', '公司官网'])
    for i in data_list:
        sheet.append(i)
    fire.save('lagou_people.xlsx')


if __name__ == '__main__':
    main()

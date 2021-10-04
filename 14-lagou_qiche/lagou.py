import requests
import time
import pymongo
import re
import json
import random
from openpyxl import Workbook

data_list = []

session = requests.session()

mongo_py = pymongo.MongoClient()

collection = mongo_py['lagou_qiche']['data']


def get_response(url, i):
    head = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "79",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "user_trace_token=20200802132537-abfafbf1-3107-4da3-92bf-09cffd883768; LGUID=20200802132539-4b2a448d-ecba-48f6-8b4b-6dfc99c2b3e4; _ga=GA1.2.188723007.1596345939; smidV2=202010261851214a13fcc215269e4236b52a7c03f6eab200002d16ba68e6690; RECOMMEND_TIP=true; _gid=GA1.2.1689631335.1610614418; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI4D8C03FB838F14C2294FCD2C5F8CAD07; WEBTJ-ID=20210114214232-177012229971ee-02ba82072b15a6-31346d-1327104-1770122299820e; LGSID=20210114214232-9f25ddb9-8153-4935-a6fc-73353a58a006; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1610614168,1610631753; TG-TRACK-CODE=gongsi_list; X_HTTP_TOKEN=3a3d96e68175d001234436016101b0fe1a594247dd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22173ada1f4436a-08f8c0a833b764-3323765-1327104-173ada1f4448ac%22%2C%22%24device_id%22%3A%22173ada1f4436a-08f8c0a833b764-3323765-1327104-173ada1f4448ac%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2287.0.4280.141%22%7D%7D; _gat=1; LGRID=20210114222713-3aef25e7-919a-4d17-a2c7-3538ccd20c1c; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1610634434",
        "origin": "https://www.lagou.com",
        "referer": "https://www.lagou.com/gongsi/0-0-43-0?isShowMoreIndustryField=true&sortField=1",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "x-anit-forge-code": "0",
        "x-anit-forge-token": "None",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "first": "false",
        "pn": i,
        "sortField": "1",
        "havemark": "0"
    }
    response = session.post(url, headers=head, data=data)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    data = re.findall(r'"result":(.*?),"totalCount"', response)[0]
    data = json.loads(data)
    for item in data:
        collection.insert_one({
            "公司名": item["companyFullName"],
            "招聘人数": item["positionNum"],
            "地址": item["city"],
            "投资轮次": item["financeStage"],
            "公司人数": item["companySize"]
        })
        # data_list.append(
        #     [item["companyFullName"], item["positionNum"], item["city"], item["financeStage"], item["companySize"]])


def main():
    # 随机延时
    # time.sleep(random.uniform(1, 4))
    # 代填入网址
    # url = "https://www.lagou.com/gongsi/0-0-43-0.json"
    # for i in range(1, 21):
    #     time.sleep(2)
    #     print(i)
    #     response = get_response(url, i)
    #     parse_data(response)

    for item in collection.find():
        data_list.append(
            [item['公司名'], item['招聘人数'], item['地址'], item['投资轮次'], item['公司人数']])
    fire = Workbook()
    sheet = fire.active
    sheet.append(['公司名', '招聘人数', '地址', '投资轮次', '公司人数'])
    for i in data_list:
        sheet.append(i)
    fire.save('lagou.xlsx')


if __name__ == '__main__':
    main()

import requests
from lxml import etree
from openpyxl import Workbook
import time
basic_url = "https://e.huawei.com/en/case-studies?page="
data_number = []



def get_response(url):
    # data = {
    #     "pageindex": 1,
    #     "region": "%7B398176B8-D7A2-4877-9F5E-893F0385316B%7D%2C",
    #     "product": "",
    #     "industry": "",
    #     "keywords": ""
    # }
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Cookie": "_ha_id..2643 = b1a089cfc6895b35;_ha_ses..2643 = f11f4fecf74e1fc4b5b514bd765c8c8b7846f9bf;channel_name = direct;channel_category = direct;_ga = GA1.2.1203867134.1605345195;_gid = GA1.2.1468692558.1605345195;Hm_lvt_48e5a2ca327922f1ee2bb5ea69bdd0a6 = 1605345195;ebg1# lang=en; ASP.NET_SessionId=zm35gumb5vdjzgu412obzete; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22c6ed4dc7-8fe8-4916-9a7f-9c3ff7a99d3d%22%2C%22options%22%3A%7B%22end%22%3A%222021-12-16T09%3A13%3A16.124Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-609951-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; layout-toobar=close-help; utag_main=v_id:0175c607b1650010e3ec233cbc3d03073003806b00978$_sn:4$_se:43$_ss:0$_st:1605370842809$dc_visit:4$ses_id:1605364560808%3Bexp-session$_pn:43%3Bexp-session$dc_event:43%3Bexp-session$dc_region:ap-northeast-1%3Bexp-session; Hm_lpvt_48e5a2ca327922f1ee2bb5ea69bdd0a6=1605369043"
    }
    response = requests.post(url, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    data = etree.HTML(response)
    texts = data.xpath('//div[@id="container"]/div[2]')
    for text in texts:
        for j in range(1, 13):
            data_list = []
            title = text.xpath('div[2]/div[' + str(j) + ']/a/div[2]/h4/text()')[0]
            data_list.append(title)
            content = text.xpath('div[2]/div[' + str(j) + ']/a/div[2]/p/text()')
            if content == []:
                content = ""
            else:
                content = content[0]
            data_list.append(content)
            data_number.append(data_list)


def main():
    for i in range(1, 41):
        url = basic_url + str(i)
        print(url)
        data = get_response(basic_url)
        parse_data(data)
        print(data_number)
        time.sleep(0.5)


if __name__ == '__main__':
    main()

file = Workbook()
sheet = file.active
for m in data_number:
    sheet.append(m)
file.save("4.xlsx")

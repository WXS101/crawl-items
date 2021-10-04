import requests
from lxml import etree
from openpyxl import Workbook

data_number = []


def get_response(page):
    url = "http://fuwu.rsj.beijing.gov.cn/nwesqintegralpublic/settlePerson/tablePage"
    data = {
        "name": "",
        "rows": "100",
        "page": page
    }
    head = {
        "Cookie": "JSESSIONID=FWM5n7oRaZropqKdlSDbHTVTM5YH7HupY0u4JXFXh5z-m57igvs2!-473531276; UqZBpD3n3n2ZW104sQY@=v1GMaGSQ@@1YW; _gscu_292366225=02989579h8b0o099; _gscbrs_292366225=1; _trs_ua_s_1=kgeilvdm_365_5p6; _trs_uv=kgeilvdm_365_3ale; _va_ref=%5B%22%22%2C%22%22%2C1602989580%2C%22http%3A%2F%2Ffuwu.rsj.beijing.gov.cn%2F%22%5D; _va_ses=*; TRACKID=a21207d4ee4eae792c00ad35e06ce3d2; _va_id=04e562b131c21508.1602559110.2.1602993224.1602989580.; _gscs_292366225=02989579uyq0fh99|pv:15",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    }
    response = requests.post(url, headers=head, data=data, timeout=10).text
    return response


def get_data(response, number):
    data_list = []
    data = etree.HTML(response)
    numbers = data.xpath('//*[@class="blue_table1"]/tbody/tr[' + str(number) + ']/td[1]/text()')[0]
    data_list.append(numbers)
    name = data.xpath('//*[@class="blue_table1"]/tbody/tr[' + str(number) + ']/td[2]/text()')[0]
    data_list.append(name)
    birth = data.xpath('//*[@class="blue_table1"]/tbody/tr[' + str(number) + ']/td[3]/text()')[0]
    data_list.append(birth)
    address = data.xpath('//*[@class="blue_table1"]/tbody/tr[' + str(number) + ']/td[4]/text()')[0]
    data_list.append(address)
    score = data.xpath('//*[@class="blue_table1"]/tbody/tr[' + str(number) + ']/td[5]/text()')[0]
    data_list.append(score)
    data_number.append(data_list)


for i in range(60, 61):
    response = get_response(i * 100)
    for j in range(1, 33):
        print(j)
        get_data(response, j)
    print(data_number)

file = Workbook()
sheet = file.active
for i in data_number:
    sheet.append(i)
file.save("2.xlsx")

"""
publications.ti_en,publications.ti_fr,publications.ti_de,publications.ct,publications.pn,publications.pn_docdb,publications.pd,oprid_full.untouched,opubd_full.untouched,publications.abs_en,publications.in,publications.pa,publications.app_fdate.untouched,publications.famn,publications.ci_cpci,publications.ca_cpci,publications.cl_cpci,publications.ipc_icai,publications.ipc_ican


1oazu8-grolz1-TTT-000055
yw1w5w-21j527-TTT-000055

dgn0lr-txnmc4-TTT-000049
zmyl23-kvsjvg-TTT-000049

"""
import requests
import random
from lxml import etree
import time
import execjs


def get_response(url, a, b):
    head = {
        "Accept": "multipart / form - data",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh;,q = 0.9, en - US;,q = 0.8, en;,q = 0.7",
        "Cookie": "cpcops_settings=%7B%22display_tree%22%3Atrue%2C%22show-2000-series%22%3A%22state-1%22%7D; JSESSIONID=DoHffAGmtQCv89BVlbV9xuUv.espacenet_levelx_prod_1",
        "EPO - Trace - Id": a+"-"+b+"-TTT-000055",
        "Host": "worldwide.espacenet.com",
        "Connection": "keep - alive",
        "Referer": "https://worldwide.espacenet.com/patent/search/family/068884128/publication/CN209821634U?q=nftxt%20%3D%20%22%E9%80%9A%E4%BF%A1%22%20AND%20pd%20%3D%20%222019%22&queryLang=en%3Ade%3Afr",
        "Sec - Fetch - Dest": "empty",
        "Sec - Fetch - Mode": "cors",
        "Sec - Fetch - Site": "same - origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("访问网页错误")


def parse_data(response):
    data = etree.HTML(response)
    url = data.xpath('//*[@class="prw_rup prw_meta_hsx_responsive_listing ui_section listItem"]/div/div[1]/div[2]/div[1]/div/a/@href')
    print(len(url))
    for i in url:
        print(i)


def get_js():
    with open("random.js", "r", encoding='utf-8')as f:
        jscode = f.read()
    result = execjs.compile(jscode).call('b')
    return result


def main():
    # 随机延时
    # time.sleep(random.uniform(1, 4))
    # 代填入网址
    url = "https://worldwide.espacenet.com/3.2/rest-services/search/family/068884128/aggregated/biblio"
    a = get_js()
    print(a)
    b = get_js()
    EPO = a + "-" + b + "-TTT-000055"
    print(EPO)
    # response = get_response(url, a, b)


    # result = get_js()
    # print(result)


if __name__ == '__main__':
    main()
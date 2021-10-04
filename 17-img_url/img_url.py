"""未完成"""


import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import random
import pymongo
from lxml import etree


# def get_html(url):
#     options = webdriver.ChromeOptions()
#     # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
#     options.add_experimental_option('excludeSwitches',
#                                     ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#     wb = webdriver.Chrome(r"E:\python3.8.3\Scripts\chromedriver.exe", options=options)
#     wait = WebDriverWait(wb, 10)
#     wb.get(url)


if __name__ == '__main__':
    url_1 = "http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/homePage.html"
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    wb = webdriver.Chrome(r"E:\python3.8.3\Scripts\chromedriver.exe", options=options)
    wait = WebDriverWait(wb, 10)
    try:
        wb.get(url_1)
        password_login = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]')))
        password_login.click()
        # time.sleep(15)
        a = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="annTB"]/tbody/tr[3]/td[8]/a')))
        a.click()
        b = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="list_shot"]/ul/li[1]')))
        b.click()
        c = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="list_shot"]/ul/li[2]')))
        c.click()
        d = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="list_shot"]/ul/li[3]')))
        d.click()

    except:
        pass











"""id: e48b9208782f608901783978b18f46e9
pageNum: 20
flag: 1


id: e48b9208782f608901783978b18f46e9
pageNum: 20
flag: 1

id: e48b9208782f608901783978b18f46e9
pageNum: 36
flag: 1

tmas_cookie=2272.7688.15400.0000; goN9uW4i0iKzS=5nfXh5BBgf_Kd2gkhZpGsJ4X_iGeQ2JjKojv8_CWfI4Q2eXgHe3AkxrwFC4gvj_Uog3U.5eWO9Ukb2_rFIc2r1a; 018f9ebcc3834ce269=8b357dde7d829a3b7920b3e61368be31; JSESSIONID=0000LhZXrmbivBSsGwaejjuketa:1bm104set; goN9uW4i0iKzT=53mT.tKrwF6AqqqmgMHcwGGPvXYvf0kd2IkWZ_z_fSGRyclKk0PCQ3Ffo05v0nwsIrGzV1hxDfhlYrAjcwbIozjnk9yAblReidbseorNjZfoJ23z.yaetRYJzALRP1xX5eCprXs4hQ0pyunq_IUdOJGXRBvX9J9Jm8Tj1aY1E3AcFm_qSslKUNP13yjaKnVIOUKwa4poZyxwUNE97UnuSpP9V_G5Qx.tee5_BXlXfZW1njRA0LEXycJTlxzTKvEWewJI1FK2wNLaG0LdelrMakPL15JJZqmBuJP7JEDOmaSHuDUkN_G.d3obNcZnHj81yjnX0TiOv0dq91iZQnI3Rkj

54iNBArFQOEn8_cME7Ux0Q1eQ2.x3Tvz9tu8vBKBpV9ez1zEcnyyeet_zK4_1p0iMoyrx0WNKS235kERxG57Pf2J3fQvP4AiKRpDQpaWqR.MGRKUUKPJ8XJwGcbItlwf80q46.mWANntCEiEOi1cQJDoJMSrE10bQR2tfvCHyjA6oLhEg3cuLBYMAraSBuHvF2Lzf_yuH94L.9iGGo4UhEDIGn_2SPDynlSjcR9LinaGTAMxPiVnFCsBBH9CeDqiDLPgoIo2NJh4pke1Ahgi8FzwGXZ7j.11n5iK6dvfH7aKyxlxhbpcLd8F3qXl7lDaxQg46IkUCz6URLhXV1HgLAQ4_f2DhxPwTHVUAK6n_A2y82j3VinZ95ig3pJ_l3mxb

5gHknMmPpVfXcasx0bD2gGZK.sSRmwEgsTVa8QgFeq9W2GaGpnMgxMK2_BEZilu.5e5TyCBtTxk1KGmPvyPdhQ8i8QbnPdbAq.0P5hoiOQW_.p4asuRiOfMRlwy.1JANAv83QxI7xYr3pTMHr2MZpwqFSxVk5RQafWEg.D3XGa5lEfxaRjg01121U8hPyaW6HLoICDMVPIAXOvkYvPz5aUNj70uLUh1VNIioWDDTc8Ps3qtyNV9oXzmaH.Omd6wJHNhY25r53YCT6.aB4huvOmz1NUxrisQGG6JngKIZon5CnYBoUM3u2pZG6tKbxIC5pwWjJyRMeCxCUavyEgHtV7viwWmlKvW7xDNaNKUJCF78UgNxADeNukQsWn70qxHHY


5Tj9DLlBgybHj7rsX7EX0E..KdhicSaWpd8zYImtp8Tc_Jp_aKMWxqfSuZaYzK3GOdkFc968QhF6hmHB5G48T7PsKU0zn0_F5ltu5252nggJBvV0czUs3up6718AuxF_t.ICQmIzcURmotzQqAbmxNtcrtNbbijAHwvFye4gP7mdSkETbcG9UMwpufVulqbQ6oMXnxaPFVsTqWus6qAJIhBBV6IVqZBsHS5gT1v37Q9GpSICWQELJjb2shSnas3iCAqsb7OCYMiTpgTzI3QAVjLlbQvkD97xzvhCe_spdktqAJ9MKWzjxDIEJSHLYoQ8NRQaV_XSBYf4j6_0SPAB8jsFcWJvguHIuij_OUXh0ZvYawuFV5vwwdf2awrHuyxud


5828q7pBBjM4nsT0bVBXxwz9Rpkkqy3A.39.Lqs2nOSZvsDm6llzX56rSEWaSfgv8BBJMDkTRvtliyB4xBiSHgeqp0bkpo46TL3.jAymgPDssRIcGSq1tAyqNWT8giwSBuQBsWNwXyZqqjjs5KIjZ6nBp.tnjenGYEMnK7i3Uq5qoz6GGl7ytSSrt06dObZwcTTeZxFMHoN94FVNYZmvdhPz6qpBHrmcepvokGjCGzX24zm_wZGyH_GVU9xdl5DdZCixfAHxYehz4pqukxO.nvJ7W.WMYeGqU4diG2OpQhA1M10KLuVh_cQTlhFd6as5nf_DmtFsrGXx8Q7fq1WhzUQtiYa0yAgB3d8qOEzqst3VDReSdTCnisRdKmAPM1a7c

"""
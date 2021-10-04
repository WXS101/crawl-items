import requests
from PIL import Image
import xlrd
import pymongo
from openpyxl import Workbook


# mongo_py = pymongo.MongoClient()
#
# collection = mongo_py['lianjia_sh']['data']
#
#
def main():
    #     # 把保存到mongodb的数据导出到一个列表中,再保存到lianjia.xlsx文件中
    #     data_lianjia = []
    #     for item in collection.find():
    #         data_lianjia.append([item['简介'], item['房租'], item['面积'], item['户型'], item['img_url']])
    #     print(data_lianjia)
    #     workbook = Workbook()
    #     sheet = workbook.active
    #     sheet.append(["简介", "房租", "面积", "户型", "img_url"])
    #     for i in data_lianjia:
    #         sheet.append(i)
    #     workbook.save('lianjia.xls')
    #
    #     # 生成图片
    #     img_list = []
    #     for item in collection.find():
    #         img_list.append(item['img_url'])
    #     head = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    #     }
    #     for i in range(10200):
    #         print(i)
    #         response = requests.get(img_list[i], headers=head)
    #         with open("第" + str(i + 1) + "张.jpg", "wb") as f:
    #             f.write(response.content)
    for i in range(1, 10201):
        try:
            print(i)
            image = Image.open("第" + str(i) + "张.jpg")
            resized_image = image.resize((2000, 1400), Image.ANTIALIAS)
            resized_image = resized_image.convert('RGB')
            resized_image.save("第" + str(i) + "张.jpg")
        except:
            continue


if __name__ == '__main__':
    main()

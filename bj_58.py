# 没得money得
import requests
import re


url = ('https://www.58.com/changecity.html?catepath=chuzu&catename=%E5%87%BA%E7%A7%9F&fullpath=137031&PGTID=0d3090a7-0248-d3da-9c28-32d8669a5711&ClickID=4')
response = requests.get(url).text
pattern = "[\u4e00-\u9fa5]+"
comp = re.compile('var cityList = {(.*?):"wuweixian|10232"', re.S)
data = re.findall(comp, response)
data = str(data)
regex = re.compile(pattern) #生成正则对象
results = regex.findall(data) #匹配
for result in results : #迭代遍历出内容
    print(result)
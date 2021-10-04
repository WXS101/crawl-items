"""http://scoring.ilsa.org/memorials/15122858.docx"""
import requests

for i in range(10024394, 19999999):
    doc_href = 'http://scoring.ilsa.org/memorials/'+str(i)+'.docx'
    print(doc_href)
    response = requests.get(doc_href)
    result = response.status_code
    if result == 200:
        response = response.content
        with open(''+str(i)+'.doc', 'wb')as f:
            f.write(response)
    else:
        continue

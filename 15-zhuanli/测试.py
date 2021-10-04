import execjs


def get_js():
    with open("text.js", "r", encoding='utf-8')as f:
        jscode = f.read()
    result = execjs.compile(jscode).call('a')
    return result


result = get_js()
print(result)

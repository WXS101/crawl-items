from selenium import webdriver


def login():
    driver = webdriver.Chrome(r"E:\python3.8.3\Scripts\chromedriver.exe")
    driver.get("./img.html")


if __name__ == '__main__':
    login()
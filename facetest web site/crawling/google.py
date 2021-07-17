from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()  # 크롬
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")  # 주소 가져오기
elem = driver.find_element_by_name("q")  # 검색창
elem.send_keys("조코딩")  # 검색창 입력
elem.send_keys(Keys.RETURN)  # 엔터

# 스크롤 다운
SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")  # 스크롤 높이

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 내림

    time.sleep(SCROLL_PAUSE_TIME)  # 기다림

    new_height = driver.execute_script("return document.body.scrollHeight")  # 새로운 스크롤
    if new_height == last_height:
        try:  # 마지막은 예외 처리
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # 이미지들 찾기
count = 1
for image in images:
    try:
        image.click()  # 이미지 클릭
        time.sleep(2)  # 쉬고
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute("src")  # 사진 src
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")  # 사진 저장
        count += 1
    except:
        pass

driver.close()

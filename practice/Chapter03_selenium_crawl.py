# **Chapter03_selenium_crawl.py
# * selenium 을 이용해서 페이지를 크롤링하는방법
# *

from selenium import webdriver
import time  # 모래시계같은 모듈 정지시킬수 있씀

driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

url = 'https://www.instagram.com/explore/tags/%EC%9E%A5%EB%82%9C%EA%B0%90/'
driver.get(url)  # 웹드라이버로 URL 페이지 접속
time.sleep(5)  # 5초간 waiting
# time sleep()을 사용하는 이유?
# : 웹 드라이버에서 페이지가 완전히 로딩되기 전에 page_source 를 가져오기 때문에
#  미완성된 코드로 내용을 수집하는데 한계가 있음 그래서 5초간에 시간을 주고
# 페이지가 전부 로딩되면 그때 소스를 가져오도록 하기 위함

page_code = driver.page_source  # 해당 URL 의 전체소스코드 가져오기
print(page_code)










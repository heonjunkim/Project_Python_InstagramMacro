# **Chapter02 webdriver.py
# * selenium webdriver 사용방법(-Chrome Driver)
# *


from selenium import webdriver

# intsagram 페이지에서 원하는 해쉬태그로 selenium 접속(-크롬 드라이버)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')   # 상대주소

# https://www.instagram.com/explore/tags/%EC%9E%A5%EB%82%9C%EA%B0%90/장난감/
# url 주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%EC%9E%A5%EB%82%9C%EA%B0%90/'
driver.get(url)
# driver.close() # 실행후 브라우저 종료


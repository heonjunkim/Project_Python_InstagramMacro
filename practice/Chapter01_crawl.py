# ** Chapter01_crawl.py
# * requests 로 크롤링하는 부분을 모듈화
# * Import 해서 사용하는 코드
# *


from libs.crawler import crawl

# 수집하고 싶은 인스타그램의 #해시태그 페이지 url주소
url = 'https://www.instagram.com/explore/tags/%EC%9E%A5%EB%82%9C%EA%B0%90/'

pageString = crawl(url)
print(pageString)
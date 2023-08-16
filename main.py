import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("LOAD_SERVER_URL")

chrome_options = webdriver.ChromeOptions()

# 첫 번째 브라우저를 생성하고 URL에 접속.
my_crawling_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
my_crawling_browser.get(url=URL)

# 동일한 URL을 각각의 탭에서 열도록 브라우저 창을 생성.
# 각 탭에서 URL을 열 때마다 새로운 창 핸들을 출력.
window_handles = [my_crawling_browser.current_window_handle]  # 첫 번째 탭의 핸들을 저장

for _ in range(3):  # 9개의 추가 탭 생성
    my_crawling_browser.execute_script("window.open()")
    window_handles.append(my_crawling_browser.window_handles[-1])  # 새 탭의 핸들을 저장
    my_crawling_browser.switch_to.window(window_handles[-1])  # 새 탭으로 스위치
    my_crawling_browser.get(url=URL)  # 동일한 URL을 열기

print(window_handles)

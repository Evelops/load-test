import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from dotenv import load_dotenv

load_dotenv()

# firefox용 브라우저 옵션 설정
firefox_options = Options()
# fake media stream 으로 미디어 스트림을 허용했다고 가정
# Firefox의 경우 media.navigator.permission.disabled 옵션을 사용해서 미디어 스트림 정보를 직접 받아오는 케이스를 씹음
firefox_options.set_preference("media.navigator.permission.disabled", True)

# Firefox WebDriver 생성
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=firefox_options)

# 탭 개수 지정
desired_tab_count = 25

# load test target URL
url = os.getenv("LOAD_SERVER_URL")

# 원하는 탭 개수만큼 반복
for _ in range(desired_tab_count):
    # 새로운 탭 열기
    driver.execute_script("window.open()")

# 사전에 탭 생성후 전환하며 URL 로드
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    driver.get(url)
    time.sleep(3)  # 3초 대기

time.sleep(10)  # 브라우저 오픈 후 10초 대기

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv

load_dotenv()

# 브라우저 옵션 설정
chrome_options = Options()
# fake media stream 으로 미디어 스트림을 허용했다고 가정
chrome_options.add_argument("--use-fake-ui-for-media-stream")

# Chrome WebDriver 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 탭 개수 지정
desired_tab_count = 20

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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 使用WebDriver管理器初始化Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开网申页面
url = 'https://app.careerpuck.com/job-board/lyft/job/7608809002?gh_jid=7608809002&utm_source=Simplify&ref=Simplify'
driver.get(url)

# 使用显式等待
wait = WebDriverWait(driver, 30)  # 增加等待时间到30秒

def fill_field(locator, value, field_name):
    try:
        field = wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)
        print(f"{field_name} 填写成功")
    except Exception as e:
        print(f"填写 {field_name} 时发生错误: {e}")

try:
    # 等待iframe加载并切换到iframe
    iframe = wait.until(EC.presence_of_element_located((By.ID, "grnhse_iframe")))
    driver.switch_to.frame(iframe)
    print("成功切换到iframe")

    # 等待表单加载
    wait.until(EC.presence_of_element_located((By.ID, "application_form")))
    print("表单已加载")

    # 填写表单字段
    fill_field((By.ID, "first_name"), 'Huapeng', 'First Name')
    fill_field((By.ID, "last_name"), 'Zhou', 'Last Name')
    fill_field((By.ID, "email"), 'zhouhp.me@gmail.com', 'Email')
    fill_field((By.ID, "phone"), '2132457077', 'Phone')


except TimeoutException:
    print("页面加载超时")
except Exception as e:
    print(f"发生错误: {e}")

finally:
    time.sleep(5)  # 等待5秒以便查看结果
    driver.quit()
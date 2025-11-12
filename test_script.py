import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

# 初始化 WebDriver
try:
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5) 
    print("--- [自动化测试脚本开始执行] ---")
    print(f"目标网站: https://www.saucedemo.com/")
    
    # --- 对应 Test Case: TC-001 (成功登录) ---
    print("\n[正在执行 TC-001: 成功登录] ...")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) 
    print("TC-001 预期: 成功登录并跳转到商品页。")
    print(f"TC-001 实际URL: {driver.current_url}")

    # --- 对应 Test Case: TC-003 (添加购物车) ---
    print("\n[正在执行 TC-003: 添加购物车] ...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2) # 暂停2秒
    print("TC-003 预期: 成功添加商品并进入购物车页面。")
    print(f"TC-003 实际URL: {driver.current_url}")

    # --- 对应 Test Case: TC-004 (登出) ---
    print("\n[正在执行 TC-004: 登出] ...")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1) 
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2) 
    print("TC-004 预期: 成功登出并返回登录页。")
    print(f"TC-004 实际URL: {driver.current_url}")

    # --- 对应 Test Case: TC-002 (失败登录) ---
    print("\n[正在执行 TC-002: 失败登录] ...")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) 
    # 抓取错误信息
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    print("TC-002 预期: 登录失败，停留在登录页并显示错误信息。")
    print(f"TC-002 实际URL: {driver.current_url}")
    print(f"TC-002 实际错误信息: {error_message}")

    print("\n--- [所有测试脚本执行完毕] ---")

except Exception as e:
    print(f"\n--- [测试执行过程中发生错误] ---")
    print(f"错误详情: {e}")
    print("请检查你的 DRIVER_PATH 是否设置正确，以及 Chrome 浏览器是否能正常打开。")

finally:
    print("\n5秒后自动关闭浏览器...")
    time.sleep(5)
    if 'driver' in locals():
        driver.quit()
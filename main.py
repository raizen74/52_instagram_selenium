import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.instagram.com/"
EMAIL = YOUR EMAIL ACCOUNT
PASSWORD = YOUR PASSWORD
ACCOUNT = "https://www.instagram.com/chefsteps/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# LOGIN ON INSTAGRAM
time.sleep(5)
email = driver.find_element("name", "username")
email.send_keys(EMAIL)
password = driver.find_element("name", "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# TARGET ACCOUNT
time.sleep(5)
driver.get(ACCOUNT)
time.sleep(2)
driver.find_element("xpath", '//a[@href="/chefsteps/followers/"]').click()

# SCROLL DOWN FOLLOWERS
time.sleep(2)
scr1 = driver.find_element(
    "xpath", "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
)
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
    time.sleep(2)

# CLICK FOLLOW
buttons = scr1.find_elements("tag name", "button")
for button in buttons:
    try:
        button.click()
        time.sleep(2)
    except ElementClickInterceptedException:  # Account already followed
        cancel_button = driver.find_element(
            "xpath", "/html/body/div[5]/div/div/div/div[3]/button[2]"
        )
        cancel_button.click()

driver.quit()

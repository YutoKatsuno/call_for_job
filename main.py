from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

# Get environment variables
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

# Initialize selenium
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3282857100&f_AL=true&geoId=101355337&keywords=Python%E9%96" \
      "%8B%E7%99%BA%E8%80%85&location=%E6%97%A5%E6%9C%AC&refresh=true "
driver_path = "/Users/katsunoyuutou/Development/chromedriver"
chrome_service = service.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)

# Go to login page
time.sleep(2)
login_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_page.click()

# Wait for the next page to load.
time.sleep(5)

# log in
mail = driver.find_element(By.NAME, "session_key")
mail.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

# Get the job list
time.sleep(5)
job_num = 0
job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in job_list[:5]:

    # Click
    time.sleep(3)
    job_num += 1
    print(job_num)
    try:
        job_link = job.find_element(By.CSS_SELECTOR, "a.job-card-container__link")
        job_link.click()
    except ElementClickInterceptedException:
        print("click()でエラーが発生しました")
        continue

    # Keep
    time.sleep(3)
    try:
        keep_button_condition = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button span")
        if keep_button_condition.text != "保存済み":
            keep_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
            keep_button.click()
    except NoSuchElementException:
        print("保存できなかった")
        continue

    # Follow
    time.sleep(3)
    try:
        follow_button_condition = driver.find_element(By.CSS_SELECTOR, "button.follow span")
        if follow_button_condition.text != "フォロー中":
            follow_button = driver.find_element(By.CSS_SELECTOR, "button.follow")
            follow_button.click()
    except NoSuchElementException:
        print("フォローできなかった")
        continue
    except ElementClickInterceptedException:
        print("フォローできなかった")
        continue

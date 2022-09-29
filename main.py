from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
login_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_page.click()

# Wait for the next page to load.
time.sleep(2)

# log in
mail = driver.find_element(By.NAME, "session_key")
mail.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()




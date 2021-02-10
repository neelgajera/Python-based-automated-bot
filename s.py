from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random

class facebook():
    def __init__(self,username,password):
        self.name = username
        self.pwd = password
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--profile-directory=Default')

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
        self.driver.get('https://www.facebook.com/')
        username_box = self.driver.find_element_by_id('email') 
        username_box.send_keys(self.name)
        password_box = self.driver.find_element_by_id('pass') 
        password_box.send_keys(self.pwd)
        login_box = self.driver.find_element_by_name('login') 
        login_box.click()
        print("login")
        

    def addFriend(self):
        self.driver.get('https://www.facebook.com/friends')
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rtmu0sqt"))
        )
        self.driver.find_element_by_css_selector("div[aria-label='Add Friend']").click()
    def updateStatus(self,massage="hello world"):
        self.driver.get('https://www.facebook.com/stories/create/')
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"div[aria-label='Stories creation form']"))
        )
        self.driver.find_element(By.XPATH, '//div[text()="Create a Text Story"]').click()
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
        )
        element.send_keys(massage)
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Share to Story']").click()

    def commant(self,massage="test"):
        self.driver.get('https://www.facebook.com/')
        element = self.driver.find_element(By.CSS_SELECTOR,"div[data-visualcompletion='ignore-dynamic']")
        lnks = element.find_element_by_tag_name("a").get_attribute("href")
        self.driver.get(lnks+"friends")
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,"a[aria-hidden='true'][role='link']"))
        )
        self.driver.get(random.choice(element).get_attribute('href'))   
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"div[aria-label='Write a comment']"))
        )
        element.send_keys(massage)
        element.send_keys(Keys.ENTER)

    def __del__(self): 
       self.driver.close()
       self.driver.quit()

       


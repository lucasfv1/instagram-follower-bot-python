from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"
# Change instagram account name in URL
SIMILAR_ACCOUNT = "https://www.instagram.com/instagram_account_name/"
# Insert username
USERNAME = "instagram user"
# Insert password
PASSWORD = "instagram password"
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower():
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self, instaUrl, instaUsername, instaPassword):
        self.driver.get(instaUrl)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(instaUsername)
        password.send_keys(instaPassword)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self, similarInstaUrl):
        time.sleep(5)
        self.driver.get(similarInstaUrl)

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)

        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(INSTAGRAM_LOGIN_URL, USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
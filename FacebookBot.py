from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tqdm import tqdm
import common
import requests
import os


class FacebookBot():
    def __init__(self):
        CHROME_OPTIONS = webdriver.ChromeOptions()
        # Turn off ask Chrome want to allow notifiations
        CHROME_OPTIONS.add_argument("--disable-notifications")
        CHROME_OPTIONS.add_argument('log-level=3')  # disable console warning
        CHROME_OPTIONS.add_experimental_option(
            "detach", True)  # Keep browser open when we done
        # CHROME_OPTIONS.add_argument('--headless')  # Run without browser
        CHROME_DRIVER = './chromedriver.exe'

        self.browser = webdriver.Chrome(
            executable_path=CHROME_DRIVER, options=CHROME_OPTIONS, service_log_path=os.devnull)
        self.browser.get(url="https://facebook.com")
        self.wait = WebDriverWait(self.browser, 20)
        self.loginBotAccount()

    def loginBotAccount(self):
        EMAIL = input("\nEnter your username: ")
        PASSWORD = input("Enter your password: ")

        self.browser.find_element_by_id("email").send_keys(EMAIL)
        submit = self.browser.find_element_by_id("pass")
        submit.send_keys(PASSWORD)
        submit.send_keys(Keys.ENTER)

        # --- Check login correct or not ---
        try:
            isCredentialCorrect = self.wait.until(
                expected_conditions.visibility_of_element_located((By.ID,'pass')))
        except:
            isCredentialCorrect = True

        if isCredentialCorrect == True:
            # --- Check have 2 Factor-Authentication ? ---
            try:
                isVerify = self.wait.until(expected_conditions.visibility_of(
                    self.browser.find_element_by_id("approvals_code")))
            except:
                isVerify = False

            if isVerify:
                VERIFY_CODE = input("\nEnter your code: ")
                isVerify.send_keys(VERIFY_CODE)
                isVerify.send_keys(Keys.ENTER)
                self.wait.until(expected_conditions.visibility_of(
                    self.browser.find_element_by_id('checkpointSubmitButton'))).send_keys(Keys.ENTER)
        else:
            print('\nYour username or password is not correct !!!')
            self.loginBotAccount()

    def saveAllPhotos(self):

        friendName = input("\nEnter your friend name: ").strip()

        self.browser.get(url='https://facebook.com/'+friendName+'/photos_all')

        # Scrolldown to load all photos
        print('\nWait a minute, system is loading your photos ... \n')
        common.scrollDownToBottom(self.browser, 'document.body', True)
        wrapper = self.browser.find_element_by_xpath(
            "//div[@data-pagelet='ProfileAppSection_0']")
        listA = wrapper.find_elements_by_xpath(
            "//img[@referrerpolicy='origin-when-cross-origin']//parent::a")

        i = 0
        count = 5 if 5 < len(listA) else len(listA)
        mainWindow = self.browser.current_window_handle

        print("Total: " + str(len(listA)) + ' photos\n')

        progressBar = tqdm(total=len(listA),
                           desc='Progressing: ')  # Progress Bar
        while i < count:
            for j in range(i, count):
                # Open link in a new tab
                listA[j].send_keys(Keys.CONTROL + Keys.RETURN)

            sleep(3)  # Wating load page
            tabs = self.browser.window_handles
            for index, tab in enumerate(tabs):  # 1 loop load only 5 pics
                if(index != 0):  # leave main tab
                    self.browser.switch_to.window(tabs[index])
                    picEle = self.browser.find_element_by_xpath(
                        "//img[@data-visualcompletion='media-vc-image'][@referrerpolicy='origin-when-cross-origin']")
                    # --- Save photo from pic URL ---
                    response = requests.get(picEle.get_attribute('src'))
                    with open('./public/'+str(i+1)+'.png', 'wb') as file:
                        file.write(response.content)
                    self.browser.close()
                    # print('Saved ' + str(i+1) + '/' + str(len(listA)))
                    i = i + 1

            # Switch to Main tab every loop
            self.browser.switch_to_window(mainWindow)

            if i == count:
                count = count + 5
            if count > len(listA):
                count = len(listA)
            progressBar.update(5)

        progressBar.close()
        print('\nAll done !!! See your photos at ./public/')

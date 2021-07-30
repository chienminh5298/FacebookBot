from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import modules
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
        self.browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=CHROME_OPTIONS, service_log_path=os.devnull)
        self.browser.get(url="https://facebook.com")
        self.wait = WebDriverWait(self.browser, 5)
        self.loginBotAccount()

    def quit(self):
        self.browser.quit()

    def loginBotAccount(self):
        # EMAIL = input("\nEnter your username: ")
        # PASSWORD = getpass('Enter your password: ')
        EMAIL = 'binarystillhere@gmail.com'
        PASSWORD = 'ChienMinh1@#$$#@!522988'

        self.browser.find_element_by_id("email").send_keys(EMAIL)
        submit = self.browser.find_element_by_id("pass")
        submit.send_keys(PASSWORD)
        submit.send_keys(Keys.ENTER)

        # --- Check login correct or not ---
        try:
            isCredentialCorrect = self.wait.until(
                expected_conditions.visibility_of_element_located((By.ID, 'pass')))
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
        modules.saveAllPhotos(self)

    def spamBot():
        modules.spamBot()
    
    def photoAnalyze(self):
        modules.photoAnalyze(self)
    
    def saveInstagramPhotos(self):
        modules.saveInstagramPhotos(self)
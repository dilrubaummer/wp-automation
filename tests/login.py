from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
#module not found
import sys
sys.path.append('/Applications/Python_automation/') #system Path
#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from pages.loginPage import LoginPage
from pages.attributePage import AttributePage
#create test report generator
import HtmlTestRunner

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(ChromeDriverManager().install())
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()
		# driver = webdriver.Chrome(executable_path=)

	def test_login_valid(self):

		driver = self.driver
		driver.get("http://localhost:8888/code-test-site/wp-admin/")

		login  = LoginPage(driver)
		login.enter_username("test_site")
		login.enter_password("test_site@123")
		login.click_login()

		attribute = AttributePage(driver)
		attribute.open_create_attribute()

		time.sleep(2)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("test Completed")

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= '/Applications/Reports'))


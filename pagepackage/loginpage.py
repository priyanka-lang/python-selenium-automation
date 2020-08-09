from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilpackage.util import Util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Loginpage():

 URL = 'https://opensource-demo.orangehrmlive.com'

 def __init__(self, browser):
     self.browser = browser

 def load(self):
     self.browser.get(self.URL)

 def login(self, username, password):
     util_page = Util(self.browser)
     util_page.findElement("id","txtUsername", username)
     util_page.findElement("id","txtPassword", password)
     util_page.findElement("id","btnLogin", "")




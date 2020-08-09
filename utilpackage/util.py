from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import inspect
from loggingpackage import loggingfile

class Util():

 log = loggingfile.customLogger(logging.DEBUG)

 def __init__(self, browser):
     self.browser = browser

 def findElement(self,elementType, element, elementName):
     self.log.info(elementType)
     if elementType == "id":
         get_element = self.browser.find_element_by_id(element)
     elif elementType == "name":
         get_element = self.browser.find_element_by_name(element)
     elif elementType == "xpath":
         get_element = self.browser.find_element_by_xpath(element)
     elif elementType == "link_text":
         get_element = self.browser.find_element_by_link_text(element)
     elif elementType == "partial_link_text":
         get_element = self.browser.find_element_by_partial_link_text(element)
     elif elementType == "tag_name":
         get_element = self.browser.find_element_by_tag_name(element)
     elif elementType == "class_name":
         get_element = self.browser.find_element_by_class_name(element)
     elif elementType == "css_selector":
         get_element = self.browser.find_element_by_css_selector(element)
     else:
         print("not a valid locator")

     get_element.click()
     self.log.info("Just an information"+"  " + element  +"  "+ "is clicked")
     get_element.send_keys(elementName + Keys.RETURN)







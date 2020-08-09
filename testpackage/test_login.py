import pytest
from pagepackage.loginpage import Loginpage
from setuppackage.browsersetup import browser


# py.test -v -s --html=report.html --self-contained-html testpackage/test_login.py
# py.test -v -s --html=.\reports\report.html --self-contained-html testpackage/test_login.py

def test_login(browser):
  login_page = Loginpage(browser)
  login_page.load()
  login_page.login("Admin","admin123")


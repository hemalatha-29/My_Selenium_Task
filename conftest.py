import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def browser():
    s = Service(r"C:\Users\Hemalatha\Downloads\chromedriver-win64 (13)\chromedriver-win64\chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    yield browser
    browser.quit()

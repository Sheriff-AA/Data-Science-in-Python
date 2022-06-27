from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "C:\Users\SHERIF ATITEBI O\Desktop\chromedriver_win32\chromedriver.exe"


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

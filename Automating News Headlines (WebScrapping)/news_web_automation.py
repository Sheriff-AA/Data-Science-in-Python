from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now()
recent_date = now.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\SHERIF ATITEBI O\Desktop\chromedriver_win32\chromedriver.exe"

# Headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
sub_titles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').get_attribute("textContent")
    sub_title = container.find_element(by="xpath", value='./a/p').get_attribute("textContent")
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)


dict = {'titles': titles, "subtitles": sub_titles, "links": links}
headlines = pd.DataFrame(dict)
file_name = f"headline-{recent_date}.csv"
final_path = os.path.join(application_path, file_name)

headlines.to_csv(final_path)

driver.quit()

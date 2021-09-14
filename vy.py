import argparse # beautiful CLI program
from bs4 import BeautifulSoup # handles traversing DOM
from datetime import datetime, date, timedelta # handles time
from selenium import webdriver # handles webscraping
# Handles selenium wait for page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time # handles timeout and wait

# Firefox selenium setup
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

# Hardcoded locations
LOCATION = {
    "trondheim": {"sted": "Trondheim S", "pos": "63.436279,10.399123"},
    "lillehammer": {"sted": "Lillehammer stasjon", "pos": "61.114912,10.461479"}
}
TIMEOUT = 10 # seconds

# Parsed inputs
afrom = "trondheim"
ato = "lillehammer"
n = 2
timestamp = "2021-09-17"
timestamp = datetime.strptime(timestamp, "%Y-%m-%d").date()

def visitUrl(url, timestamp):
    driver.get(url)
    date_tag = datetime.strftime(datetime.strptime(str(timestamp), "%Y-%m-%d").date(), "%d.%m.%Y")
    try:
        WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, 'date-tag-'+date_tag)))
    except TimeoutException:
        print("Timed out waiting for page to load!")
        return
    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    travel_suggestions = soup.select('li[aria-label*="Reise"]')
    # print(travel_suggestions)
    for li in travel_suggestions:
        div = li.find_all('div')[0]
        span = div.find_all('span')
        travel_time = span[0].get_text()
        travel_duration = span[4].get_text()
        price = "".join(span[-1].get_text().split()[2:])
        print(travel_time, travel_duration, price)

# Run webscraper n-times
for i in range(2):
    print()
    print(timestamp)
    url = f"https://www.vy.no/se-reiseforslag?from={LOCATION[afrom]['sted']}&to={LOCATION[ato]['sted']}&fromDateTime={timestamp}T02:00:13.951Z&fromExternalId=NSR:NSR:StopPlace:59977&toExternalId=NSR:NSR:StopPlace:420&passengers=W3siaWQiOjYwLCJhZ2UiOm51bGwsImRpc2NvdW50cyI6W10sImNhdGVnb3J5IjoiQWR1bHQiLCJuYW1lIjoiVm9rc2VuIn1d&addons=W3sidHlwZSI6ImJpY3ljbGUiLCJudW1iZXJUb0J1eSI6MH0seyJ0eXBlIjoibGFyZ2VfYW5pbWFsIiwibnVtYmVyVG9CdXkiOjB9LHsidHlwZSI6InNtYWxsX2FuaW1hbCIsIm51bWJlclRvQnV5IjowfSx7InR5cGUiOiJzdHJvbGxlciIsIm51bWJlclRvQnV5IjowfSx7InR5cGUiOiJ3aGVlbGNoYWlyIiwibnVtYmVyVG9CdXkiOjB9XQ==&fromPosition={LOCATION[afrom]['pos']}&toPosition={LOCATION[ato]['pos']}"
    # print(url)
    visitUrl(url, timestamp)
    timestamp = timestamp + timedelta(days=1)

parser = argparse.ArgumentParser(description='A webscraper for vy.no, finding train/bus tickets from location A to B')
#parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
parser.add_argument('-f','--from', help='Description for bar argument')
parser.add_argument('-t','--to', help='Description for bar argument')
parser.add_argument('-s','--start-date', help='Description for bar argument')
parser.add_argument('-n','--n', help='Description for bar argument')
args = vars(parser.parse_args())
print(args)

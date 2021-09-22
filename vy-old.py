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
    "trondheim": {"sted": "Trondheim S", "latitude": "63.436279","longitude": "10.399123"},
    "lillehammer": {"sted": "Lillehammer stasjon", "latitude": "61.114912","longitude": "10.461479"}
}
TIMEOUT = 10 # seconds

# Parsed inputs
afrom = "trondheim"
ato = "lillehammer"
n = 2
timestamp = "2021-09-17"
timestamp = datetime.strptime(timestamp, "%Y-%m-%d").date()

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

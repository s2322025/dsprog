import requests
from bs4 import BeautifulSoup
import sqlite3

dbname = "konzatu"
conn = sqlite3.connect(dbname)
cur = conn.cursor()
create_table = "create table konzatu (id text,name text)"
cur.execute(create_table)

conn.close()


url = requests.get('https://www.navitime.co.jp/congestion/prediction/result?node=00004538&from=congestion.prediction.railroad')
soup = BeautifulSoup(url.text, "html.parser")

konzatu_date = []
for e in soup.find_all('dt',class_ = "week-date-text"):
    konzatu_date.append(e.getText().replace("\n", ""))

konzatu = []
for e in soup.find_all('span',class_ = "blue week-status-text"):
    konzatu.append(e.getText().replace("\n", ""))

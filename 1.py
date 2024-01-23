import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.navitime.co.jp/congestion/prediction/result?node=00004538&from=congestion.prediction.railroad')
soup = BeautifulSoup(url.text, "html.parser")

konzatu_date = []
for e in soup.find_all('dt',class_ = "week-date-text"):
    konzatu_date.append(e.getText().replace("\n", ""))

print(konzatu_date)

konzatu = []
for e in soup.find_all('span',class_ = "blue week-status-text"):
    konzatu.append(e.getText().replace("\n", ""))

print(konzatu)
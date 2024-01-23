import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.navitime.co.jp/congestion/prediction/result?node=00004538&from=congestion.prediction.railroad')
soup = BeautifulSoup(url.text, "html.parser")
for e in soup.find_all('dt',class_= "week-date-text"):
    print(e.getText())
# -*- coding: utf-8 -*-
import os
import datetime
import csv
import urllib.request
from bs4 import BeautifulSoup

def str2float(weather_data):
    try:
        return float(weather_data)
    except:
        return 0

def scraping(url, date):

    # 気象データのページを取得
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, features='html.parser')
    trs = soup.find("table", {"class": "data2_s"})

    data_list_per_hour = []

    # table の中身を取得
    for tr in trs.findAll('tr')[2:]:
        tds = tr.findAll('td')

        if tds[1].string is None:
            break

        data_dict = {
            "年月日": date,
            "時間": tds[0].string,
            "気圧（現地）": str2float(tds[1].string),
            "気圧（海面）": str2float(tds[2].string),
            "降水量": str2float(tds[3].string),
            "気温": str2float(tds[4].string),
            "露点湿度": str2float(tds[5].string),
            "蒸気圧": str2float(tds[6].string),
            "湿度": str2float(tds[7].string),
            "風速": str2float(tds[8].string),
            "風向": str2float(tds[9].string),
            "日照時間": str2float(tds[10].string),
            "全天日射量": str2float(tds[11].string),
            "降雪": str2float(tds[12].string),
            "積雪": str2float(tds[13].string),
        }

        data_list_per_hour.append(data_dict)

    return data_list_per_hour

def create_dataset():

    # 出力ファイル名
    output_file = "weather.csv"

    # データ取得開始・終了日
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 13)

    # CSV の列
    fields = ["年月日", "時間", "気圧（現地）", "気圧（海面）",
              "降水量", "気温", "露点湿度", "蒸気圧", "湿度",
              "風速", "風向", "日照時間", "全天日射量", "降雪", "積雪"]  # 天気、雲量、視程は今回は対象外とする

    dataset = []

    with open(os.path.join(output_dir, output_file), 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(fields)

        date = start_date
        while date != end_date + datetime.timedelta(1):

            # 対象url
            url = "https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?" \
                  "prec_no=43&block_no=47626&year=%d&month=%d&day=%d&view=" % (date.year, date.month, date.day)

            data_per_day = scraping(url, date)

            for dpd in data_per_day:
                writer.writerow([dpd[field] for field in fields])
                dataset.append(dpd)

            date += datetime.timedelta(1)

    return dataset

if __name__ == '__main__':
    dataset = create_dataset()

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

start_date = pd.Timestamp("2022-02-24")
end_date = pd.Timestamp("2023-01-25")
data = []

for date in pd.date_range(start_date, end_date):
    year = date.year
    month = date.strftime("%B").lower()
    day = date.strftime("%#d")
    if year == 2022:
        date_string = f"{month}-{day}"
    if year == 2023:
        date_string = f"{month}-{day}-{year}"
    url = f"https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-{date_string}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"{date} data is not available.")
            continue
        soup = bs(response.content, 'html.parser')
        description = soup.find("div", {"class": "field-name-body"}).text
        description = re.sub(r'http\S+', '', description)
        description = description.lower()
        description = description.replace(" dot ", ".")
        description = description.replace("\n", " ")
        description = description.replace("\xa0", " ")
        pattern = re.compile('[^A-Za-z0-9\s]')
        description = pattern.sub("", description)
        description = description.split(".")[0]
        data.append({"Date": date.strftime("%B-%d-%Y").lower(), "Description": description})
    except (requests.exceptions.RequestException, KeyError, TypeError) as error:
        print(f"{error} for {date}")
    continue

df = pd.DataFrame(data)
df.to_csv("isw_data.csv", index=False)

import requests 
import re
from nltk.stem import PorterStemmer
import datetime
import time
from dateutil.rrule import rrule, MONTHLY

start_dt = datetime.date(2020, 1,1)
end_dt = datetime.date(2020,12,31)
dates = [(dt.year, dt.month) for dt in rrule(MONTHLY, dtstart=start_dt, until=end_dt)]
api_key="0n5Jkz9M6wknbqpYV45sO8lAO5NxzOvS"
opioid_article_dictionary = {}
for year, month in dates:
    opioid_article_list = []
    time.sleep(2)
    # 1st cell
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}'
    r = requests.get(url)
    json_data = r.json()
    #2nd cell
    headline_list = []
    article_list = json_data['response']['docs']
    for article in article_list:
        headline_list.append(article['headline']['main'])
    #3rd cell
    ps = PorterStemmer()
    for headline in headline_list:
        original_headline = headline
        headline = re.sub(r'[^\w\s]','',headline)
        headline = headline.lower()
        headline = headline.split(" ")
        
        contains_opioid = False
        # contains_crisis = False
        for word in headline:
            word = ps.stem(word)
            if word == "opioid":
                contains_opioid = True
            # elif word == "crisis":
            #     contains_crisis = True
        if contains_opioid:
            opioid_article_list.append(original_headline)
    opioid_article_dictionary[month] = opioid_article_list
print(opioid_article_dictionary)
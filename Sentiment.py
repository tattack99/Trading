### Tim Johansson
### Get sentiment
### 2020-10-19

from bs4  import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import datetime


forex_pair_links = [
"https://www.ig.com/au/forex/markets-forex/eur-sek",
"https://www.ig.com/au/forex/markets-forex/aud-usd",
"https://www.ig.com/au/forex/markets-forex/eur-chf",
"https://www.ig.com/au/forex/markets-forex/eur-gbp",
"https://www.ig.com/au/forex/markets-forex/eur-jpy",
"https://www.ig.com/au/forex/markets-forex/eur-usd",
"https://www.ig.com/au/forex/markets-forex/gbp-eur",
"https://www.ig.com/au/forex/markets-forex/gbp-jpy",
"https://www.ig.com/au/forex/markets-forex/gbp-usd",
"https://www.ig.com/au/forex/markets-forex/usd-cad",
"https://www.ig.com/au/forex/markets-forex/usd-chf",
"https://www.ig.com/au/forex/markets-forex/usd-jpy",
]

#Get sentiment for a single forex pair and save it in 
def get_sentiment(forex_pair):
    
    #Getting the time now
    correct_time_now = str(datetime.datetime.today().strftime("%Y:%m:%d-%H:%M:%S"))
    
    #Open url
    html = urlopen(forex_pair)
    
    #Creating a soup out of the link
    soup = BeautifulSoup(html , 'lxml')
    
    #Getting the sentiment procentage, direction and forex pair.
    sentiment_procent = str(soup.find('span' , attrs = {'class' : 'price-ticket__percent' }))
    sentiment_direction = str(soup.find("strong"))
    forex_pair = str(soup.find("h1" , attrs = {'class' : "ma__title" }))
    
    #Cleaning the data
    sentiment_direction_clean = sentiment_direction.replace("<strong>" , '').replace("</strong>" , '').replace("long" , 'buy').replace("short" , 'sell')
    sentiment_procent_clean = sentiment_procent.replace('<span class="price-ticket__percent">' , '').replace("</span>" , '')
    forex_pair_clean = forex_pair.replace('<h1 class="ma__title">' , '').replace("</h1>" , '')
    
    #Appending the data to a csv document
    df1 = pd.DataFrame({
                    'date' : [correct_time_now],
                    'forex' : [forex_pair_clean],
                    'sentiment' : [sentiment_procent_clean], 
                    'direction' : [sentiment_direction_clean]})
    df1.to_csv(r'C:\Users\timmo\Google Drive\1.Trading\1.Data\SentimentData.csv' , mode = "a" , header=False , index = False)
    print(df1)

#Function to see the position of the different forex pair
def check_all_major_forex_pair_sentiment():
    for forex_pair_link in forex_pair_links:
        get_sentiment(forex_pair_link)

#Start up
check_all_major_forex_pair_sentiment()















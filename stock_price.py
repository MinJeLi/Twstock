import json
from urllib.request import urlopen

class stock(object):
    
    def __init__(self, stock_number):
        self.base_url = 'https://www.twse.com.tw/rwd/en/afterTrading/STOCK_DAY?'
        self.stock_number = stock_number
        self.data = None
        self._fetch_initial_data()
        
    def _fetch_initial_data(self):
        date_url = "20231130"
        total_url = self.base_url + "date=" + date_url + "&stockNo=" + self.stock_number + "&response=json"
        try:
            self.data = json.loads(urlopen(total_url).read())
            if self.data['total'] == 0:
                print("Cannot find Stock number")
                exit()
        except Exception as e:
            print(f"Error fetching data: {e}")
            exit()
            
    def priceHistory(self):
        
        if not self.data:
            return {}

        date_of_index = self.data['fields'].index('Date')
        price_of_index = self.data['fields'].index('Closing Price')
        history_of_price = dict()
        
        for month in range(1,13):
            formatted_month = "{:02}".format(month)
            date_url = "2023"+ str(formatted_month) + "30"
            total_url = self.base_url + "date=" + date_url +"&stockNo=" + self.stock_number +"&response=json"
            data = json.loads(urlopen(total_url).read())
            try:
            
                if data['total'] == 0:
                    break
            
                for price in data['data']:
                    history_of_price[price[date_of_index]]= price[price_of_index]
                    
            except Exception as e:
                print(f"Error fetching data for month {formatted_month}: {e}")
            
        return history_of_price
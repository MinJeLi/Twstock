from stock_price import stock
from mechin import mechinL

if __name__ == '__main__':
    stock_number = input()
    history_of_price = dict()
    history_of_volume = dict()
    
    stock_instance = stock(stock_number)
    history_of_price = stock_instance.priceHistory()
    history_of_volume = stock_instance.volumeHistory()
    # print(history_of_price)
    # print(history_of_volume)
    mechinL.draw(history_of_price,history_of_volume)
    mechinL.learning(history_of_price,history_of_volume)
    
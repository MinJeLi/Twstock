from stock_price import stock
from mechin import mechinL

if __name__ == '__main__':
    stock_number = input()
    history_of_price = dict()
    
    stock_instance = stock(stock_number)
    history_of_price = stock_instance.priceHistory()
    # print(history_of_price)
    mechinL.draw(history_of_price)
    # mechinL.learning(history_of_price)
    
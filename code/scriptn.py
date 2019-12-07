# DOCUMENTATION ---------------------------------------------------
'''
Description:    Write functions to obtain stock & company data
Sources:        https://pandas-datareader.readthedocs.io/en/latest/
                https://pypi.org/project/tiingo/
'''


# IMPORT LIBRARIES ------------------------------------------------
from tiingo import TiingoClient
import matplotlib.pyplot as plt


def instantiate_conn_tiingo():
    config  = {}
    config['session'] = True
    config['api_key'] = input('Input token =>')
    client  = TiingoClient(config)



# Get Ticker


def get_stock_company_info(ticker, begin_date, end_date):
    '''
    Description:    Return information associated with the company
                    whose ticker was queries. 
    Fields:         ticker, exchangeCode, name, description, endDate, startDate
    '''
    # Get Metadata
    metadata = client.get_ticker_metadata(ticker)
    
    # Retreive Filds
    desc            = metadata['description']
    ticker          = metadata['description']
    exchangeCode    = metadata['description']
    name            = metadata['description']
    endDate         = metadata['description']
    startDate       = metadata['description']
   
    # Return 
    return metadata 


def insert_stock_company_info(conn, metadata):

    pass




def get_stock_price(ticker, begin, end):
    ticker_metadata = client.get_ticker_metadata(ticker)
    print(ticker_metadata)
    '''
    historical_prices   = client.get_ticker_price('GOOGL', 
                                                fmt='json', 
                                                startDate='2019-01-01', 
                                                endDate='2019-11-15', 
                                                frequency='daily')

    list_date   = []
    list_close  = []
    list_daily_change = []

    for data in historical_prices:
        date    = data['date']
        close   = data['close']
        high    = data['high']
        low     = data['low']
        open_   = data['open']
        volume  = data['volume']

        list_date.append(date)
        list_close.append(close)

    for a, b in zip(list_close[0:-1], list_close[1:]):
        daily_pct_change = ((b-a)/a) * 100
        list_daily_change.append((b-a/a)*100)
        print(daily_pct_change) 
    '''



'''
print('** TICKER => {}'.format('GOOGL'))
for key in historical_prices[0]:
    print('Key => {}'.format(key), historical_prices[0][key])
'''

# DOCUMENTATION --------------------------------------------------
'''
https://pandas-datareader.readthedocs.io/en/latest/
https://pypi.org/project/tiingo/
'''


# IMPORT LIBRARIES -----------------------------------------------

# Python
import pandas as pd
import mysql.connector
import os

# Project
import module0_utility_functs as m0

# CONNECTION -----------------------------------------------------

# FUNCTIONS -------------------------------------------------------

def get_snp500_tickers(mydb, mycursor):

    sql = '''SELECT ticker FROM snp_500_ticker_symbols'''
    df  = pd.read_sql(sql, mydb)

    return df

def insert_ticker_company_info(client, ticker, mydb, mycursor, begin_date, end_date):
    '''
    Description:    Return information associated with the company
                    whose ticker was queries. 
    Fields:         ticker, exchangeCode, name, description, endDate, startDate
    '''
    # Get Metadata
    metadata = client.get_ticker_metadata(ticker)

    # Retreive Filds
    ticker          = metadata['ticker']
    exchangeCode    = metadata['exchangeCode']
    name            = metadata['name']
    description     = metadata['description']
    val = [ticker, exchangeCode, name, description]


    # SQL Statements
    sql = '''INSERT IGNORE INTO snp_500_metadata (ticker, exchangeCode, name, description)
             VALUES (%s, %s, %s, %s)'''
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.errors.DatabaseError as err:
        print(err)
        list_tickers.append(val[0])


    # Logging 
    print('Insertion complete for ticker {}'.format(ticker))

    # Return val
    return [ticker, exchangeCode, name, description]



def get_snp500_tickers(mydb, mycursor):

    sql = '''SELECT symbol FROM snp_500_ticker_symbols'''
    df  = pd.read_sql(sql, mydb)

    return df


def iterate_list_tickers_insert_data():

    # Iterate list tickers
    for ticker in df_symbols[400:]:
        insert_ticker_company_info(client, ticker, mydb, mycursor, '2019-1-1', '2019-1-2')


def insert_snp_ticker_info(snp_info, mydb, mycursor):
    '''['Symbol', 'Security', 'GICS Sector', 'GICS Sub Industry',
       'Headquarters Location', 'CIK']
    '''
    Count = 0

    for row in snp_info.itertuples():
        val = [row[1], row[2], row[3], row[4], row[5], row[6]]
        sql = '''INSERT INTO snp_500_ticker_symbols 
                        (symbol, security, sector, sub_industry, headquarters, cik)
                        VALUES(%s, %s, %s, %s, %s, %s)'''

        mycursor.execute(sql, val)
        mydb.commit()
        Count +=1

    # Logging:
    print('Insertion complete for {} number of tickers'.format(Count))

    # Return
    return None






# DOCUMENTATION ----------------------------------------------------
'''
Description:    Module for utility functions
'''


# IMPORT LIBRARIES -------------------------------------------------
# Python
import pandas as pd
import mysql.connector
import os
from tiingo import TiingoClient


# FUNCTIONS --------------------------------------------------------


def instantiate_conn_mysql():

    mydb = mysql.connector.connect(
            host="localhost",
            user="ccirelli2",
            passwd=input('Mysql password'),
            database='TIINGO_STOCK_DATA'
            )
    mycursor = mydb.cursor()

    return mydb, mycursor



def instantiate_conn_tiingo():
    # Set Values to Configuration
    config  = {}
    config['session'] = True
    config['api_key'] = input('Tiingo token') 
    # Pass Configurations to TiingoClient Server / api
    client  = TiingoClient(config)
    # Return Connection
    return client

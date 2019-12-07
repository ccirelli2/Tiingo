# DOCUMENTATION --------------------------------------------------
'''
Description:    Create sql tables.  Insert Data

'''


# IMPORT LIBRARIES -----------------------------------------------

# Python
import pandas as pd
import mysql.connector
import os 
from tiingo import TiingoClient

# Project
import module0_utility_functs as    m0
import module1_sql as               m1

# INSTANTIATE CONNECTION TO TIINGO -----------------------------
client  = m0.instantiate_conn_tiingo()

# INSTANTIATE CONNECTION TO MYSQL ------------------------------
mydb, mycursor  = m0.instantiate_conn_mysql()

# DEFINE DIRECTORIES --------------------------------------------
dir_data    = r'/home/ccirelli2/Desktop/repositories/Tiingo/data'
os.chdir(dir_data)

# DATA ----------------------------------------------------------
snp_500_info    = pd.read_excel(r'snp_500.xlsx')



# FUNCTIONS -----------------------------------------------------



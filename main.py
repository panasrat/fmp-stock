import pandas as pd

from config import Config
from helpers import get_delisted_companies, get_historical_dividends, get_db_engine, write_pandas_to_mysql

def main():

    API_KEY = Config.API_KEY
    URL_DELISTED_COMPANIES = Config.URL_DELISTED_COMPANIES
    URL_HISTORICAL_DIVIDENDS = Config.URL_HISTORICAL_DIVIDENDS
    COMPANIES_TO_GET_DIVIDENDS = ['AAPL', 'TSLA']

    DB_HOST = Config.DB_HOST
    DB_USER = Config.DB_USER
    DB_PASSWORD = Config.DB_PASSWORD
    DB_NAME = Config.DB_NAME
    
    delisted_companies_df = get_delisted_companies(URL_DELISTED_COMPANIES, API_KEY)
    historical_dividends_df = get_historical_dividends(COMPANIES_TO_GET_DIVIDENDS, URL_HISTORICAL_DIVIDENDS, API_KEY)

    table_dict = {'delisted_companies': delisted_companies_df, 
                  'historical_dividends': historical_dividends_df}

    engine = get_db_engine(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    write_pandas_to_mysql(table_dict=table_dict, engine=engine, if_exists='replace')

    tables = pd.read_sql_query('show tables;', engine)
    table_list = list(tables[f'Tables_in_{DB_NAME}'])
    print(f'Tables in database {DB_NAME}: {table_list}')

if __name__ == "__main__":
    main()

    


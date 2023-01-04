# FMP Data Ingestion Project

This project is an example of how you can ingest data from https://site.financialmodelingprep.com/developer/docs/ and write it into MySQL database using Python.

There are 2 endpoints that this project covers:
1. Delisted Companies: https://financialmodelingprep.com/api/v3/delisted-companies
2. Historical Stock Dividends: https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend

Please note that the historical dividends also requires examples of stock symbol, in this case, we use `['AAPL', 'TSLA']`.

This project can be separated into 3 parts:
1. `main.py` controls is the pipeline of the ingestion.
2. `helpers.py` contains helper functions that are required.
3. `config.py` is where you can fill your own configuration and credentials.

## Run This Project

To run this project, please create `venv` using `requirements.txt` to install all dependencies and activate it. You also need to have MySQL database installed with pre-created database named "fmp-stock". And lastly, you can get `API_KEY` from https://site.financialmodelingprep.com/developer/docs/, then edit configuration in `config.py`.

After all these steps done, run the command:

```
python main.py
```

This should be all for the project.




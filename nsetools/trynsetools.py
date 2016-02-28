# Importing Driver Class for National Stock Exchange
from nsetools import Nse

# Instantiating the driver class for National Stock Exchange
nse = Nse()

# Importing Pretty Print
from pprint import pprint

pprint('Getting Index Quote for Infosys')
pprint(nse.get_quote('infy'))

pprint('Getting the entire Index List')
indices = nse.get_index_list()
pprint(indices)

pprint('Getting Index Quote for a particular index')
pprint(nse.get_index_quote(indices[1]))


pprint('Getting Index Quote for all indices')
for x in indices:
   pprint(nse.get_index_quote(x))

pprint('Getting all Stock Codes')
all_stocks = nse.get_stock_codes()
pprint(all_stocks)

pprint('Getting Quotes for each stock')
for x in all_stocks:
    pprint(nse.get_quote(x))

pprint('Getting Advances & Declines')
pprint(nse.get_advances_declines())

pprint('Getting all Top Gainers')
pprint(nse.get_top_gainers())

pprint('Getting all Top Losers')
pprint(nse.get_top_losers())


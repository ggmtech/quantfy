# Stock analysis for buying
# stock analyis for selling

# fundamental analysis for stocks

# select strong stocks

# select rising stocks

# Selecct mature stock

# Company life cycle stage # startup, unicorn, highgrowth, smallcap, midcap, stable, largecap, 

# price for the performance

# having momentum 

# Stocks with trailwinds and headwinds

# Strong stocks with momentum and tailwind and reasonablevaluation to growth

###############################################################################
''' 
# Install uv
# source $HOME/.local/bin/env (sh, bash, zsh)
# source $HOME/.local/bin/env # To add $HOME/.local/bin to your PATH
# see options by running uv
# uv --version
# $ uv self update
# Initialize projects with uv init and add dependencies with uv add package
# Run scripts with uv run script.py—no manual virtual environment activation needed
# $ uv init mydir
# command will immediately create a new mydir directory with the following contents:
├── .gitignore
├── .python-version
├── README.md
├── hello.py
└── pyproject.toml

# cd mydir

# $ uv add scikit-learn xgboost         # $ uv remove scikit-learn
# $ uv run hello.py   # Run python script

# uv.lock file and $ uv export -o requirements.txt
# uv venv
uv add package
uv pip install -r requirements.txt

uv format  # Format all Python files in the project
uv format --check  # Check formatting without making changes
uv format --diff   # Show a diff of what would change

# linking git
git init     # Initialize the local directory as a Git repository. By default, the initial branch is called main.  git init -b main

# in github , create new  and seect Push an existing local repository to GitHub 
# check git remote -v

git remote add origin <Repository_Location>
git push origin <branch_name>

'''





'''
% python3 -m ensurepip --upgrade
!pip3 install --upgrade pip
!pip3 install yfinance
'''

# import stocktests  # import files with small routines
from datetime import datetime, timedelta
import time   # for sleep function

import numpy  as np
import pandas as pd

import yfinance   as yf   # Returns data directly in pandas df/series
import yahooquery as yq


#pd.set_option('display.float_format', '{:.2f}'.format)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)


from yahoo_fin import stock_info

# Retrieve live price of Apple Inc. (AAPL)
price = stock_info.get_live_price('AAPL')

import matplotlib.pyplot as plt


import nselib     # download NSE data from NSElib

bhav20260716= nselib.capital_market.bhav_copy_equities('16-07-2026') # [3419 rows x 34 columns]
bhav20260716


###############################################################################
###############################################################################
# yfinance library data

yf.Market("EUROPE").summary #US GB ASIA  EUROPE RATES COMMODITIES CURRENCIES  CRYPTOCURRENCIES
yf.Market("US").summary
yf.Market("US").status
yf.Market("ASIA").summary
yf.Market('RATES').summary
yf.Market('COMMODITIES').summary
yf.Market('CURRENCIES').summary
yf.Market('CRYPTOCURRENCIES').summary

###############################################################################
# Set dates
end_date    = datetime.today()
start_date  = end_date        - timedelta( days=365 * 2 )  # 2 years ata for moving averages
end_date
start_date



###############################################################################
# https://dataheadhunters.com/academy/how-to-use-python-for-financial-analysis-step-by-step-guide/



# Define the stock symbol and the time period

stock_symbol = 'POLYCAB.NS'      # stock_symbol = 'AAPL'
start_date   = '2022-01-01'
end_date     = '2026-07-16'
# set the start and end dates for our market data request
# end_date    = datetime(year=2026, month=7, day=16)
# start_date  = datetime(year=2023, month=1, day= 1)







stock_symbols = []
def NSE200_data() :
    NSE200 = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "BHARTIARTL.NS", "ICICIBANK.NS", "SBIN.NS", "INFY.NS", "LICI.NS", "HINDUNILVR.NS", "ITC.NS", "LT.NS", "BAJFINANCE.NS", "MARUTI.NS", "HCLTECH.NS", "ADANIENT.NS", "AXISBANK.NS", "SUNPHARMA.NS", "M&M.NS", "NTPC.NS", "KOTAKBANK.NS", "ONGC.NS", "HAL.NS", "DMART.NS", "TITAN.NS", "ULTRACEMCO.NS", "ADANIPORTS.NS", "ADANIPOWER.NS", "ADANIGREEN.NS", "COALINDIA.NS", "POWERGRID.NS", "ASIANPAINT.NS", "BAJAJ-AUTO.NS", "WIPRO.NS", "BAJAJFINSV.NS", "SIEMENS.NS", "NESTLEIND.NS", "IOC.NS", "IRFC.NS", "JIOFIN.NS", "TATASTEEL.NS", "JSWSTEEL.NS", "DLF.NS", "BEL.NS", "VBL.NS", "TRENT.NS", "VEDL.NS",  "ABB.NS", "INDIGO.NS", 'ETERNAL.NS', "GRASIM.NS", "PFC.NS", "PIDILITIND.NS", "AMBUJACEM.NS",  "HINDALCO.NS", "GODREJCP.NS", "SBILIFE.NS", "LODHA.NS", "TATAPOWER.NS", "BANKBARODA.NS",  "GAIL.NS", "PNB.NS", "TECHM.NS", "BRITANNIA.NS", "RECLTD.NS", "EICHERMOT.NS", "BPCL.NS",  "HDFCLIFE.NS", "CIPLA.NS", "DIVISLAB.NS", "HAVELLS.NS", "INDUSINDBK.NS", "TVSMOTOR.NS",  "ADANIENSOL.NS", "CHOLAFIN.NS", "UNIONBANK.NS", "HEROMOTOCO.NS", "JSWENERGY.NS", "DABUR.NS", "TATACONSUM.NS", "CANBK.NS", "ATGL.NS", "ZYDUSLIFE.NS", "MOTHERSON.NS", "IDEA.NS", "JINDALSTEL.NS", "NHPC.NS", "POLYCAB.NS", "CGPOWER.NS", "DRREDDY.NS", "CUMMINSIND.NS", "BHEL.NS", "TORNTPHARM.NS", "SHREECEM.NS", "SHRIRAMFIN.NS", "INDUSTOWER.NS", "BAJAJHLDNG.NS", "IDBI.NS", "BOSCHLTD.NS",  "APOLLOHOSP.NS", "MANKIND.NS", "MARICO.NS", "INDHOTEL.NS", "ICICIPRULI.NS", "HDFCAMC.NS", "ICICIGI.NS", "COLPAL.NS", "NAUKRI.NS", "MAXHEALTH.NS", "GODREJPROP.NS", "IRCTC.NS", "RVNL.NS",  "TIINDIA.NS", "NMDC.NS", "LUPIN.NS", "HINDPETRO.NS", "AUROPHARMA.NS", "BHARATFORG.NS",  "SUPREMEIND.NS", "OFSS.NS", "YESBANK.NS", "INDIANB.NS", "TORNTPOWER.NS", "PRESTIGE.NS", "SRF.NS", "SBICARD.NS", "ASHOKLEY.NS", "SUZLON.NS", "OIL.NS", "CONCOR.NS", "MAZDOCK.NS", "SAIL.NS", "BALKRISIND.NS", "ABCAPITAL.NS", "DIXON.NS", "PERSISTENT.NS", "ALKEM.NS", "JSWINFRA.NS", "POLICYBZR.NS", "ASTRAL.NS", "BERGEPAINT.NS", "PIIND.NS", "BANKINDIA.NS", "IDFCFIRSTB.NS", "MRF.NS", "BDL.NS", "SJVN.NS",  "TATACOMM.NS", "PATANJALI.NS", "LTTS.NS", "AUBANK.NS", "NYKAA.NS", "VOLTAS.NS", "MAHABANK.NS", "ACC.NS", "MPHASIS.NS", "FACT.NS", "PETRONET.NS", "APLAPOLLO.NS", "TATAELXSI.NS", "ESCORTS.NS", "TATATECH.NS", "PAGEIND.NS", "KALYANKJIL.NS", "LTF.NS", "KPITTECH.NS", "UPL.NS",  "BIOCON.NS", "FEDERALBNK.NS", "SONACOMS.NS", "LICHSGFIN.NS", "BSE.NS", "COFORGE.NS", "POONAWALLA.NS", "FORTIS.NS", "M&MFIN.NS", "JUBLFOOD.NS", "DALBHARAT.NS", "ABFRL.NS", "IGL.NS", "MFSL.NS", "BANDHANBNK.NS", "DEEPAKNTR.NS", "APOLLOTYRE.NS", "GLAND.NS", "IPCALAB.NS", "DELHIVERY.NS", "SUNTV.NS", "SYNGENE.NS","TATACHEM.NS", "PAYTM.NS", "LAURUSLABS.NS", "LALPATHLAB.NS", "ZEEL.NS","UNITDSPR.NS"]
    return NSE200



# Get NSE500 using nselib     
dir(nselib.capital_market) # bhav_copy_with_delivery','bhav_copy_sme', 'nifty50_equity_list',  'niftymidcap150_equity_list', 'niftynext50_equity_list', 'niftysmallcap250_equity_list',

NSE150smallcap = nselib.capital_market.niftysmallcap250_equity_list()

NSEmidcap150 = nselib.capital_market.niftymidcap150_equity_list()

nifty50_equity_list = nselib.capital_market.nifty50_equity_list()
nifty50_equity_list

bhav20260717= nselib.capital_market.bhav_copy_equities('17-07-2026') # [3419 rows x 34 columns]
bhav20260717




###############################################################################


NSE200_data()

# download market price data for a single/multiple ticker OHLCV, # group_by="column" 
df_multi = yf.download(tickers  = NSE200_data(), # stock_symbols,  # can be list of stocke []
                        start    = start_date,
                        end      = end_date,
                       # period   = "max"
                        interval = "1d", # [1,2,5,15,30,60, 90]m, 1d, 1wk,1mo # intraday <2month
                        group_by = "ticker", #'ticker'or'OHLV' on top column 'Level 1' MultiIndex
                        auto_adjust=True,    # Auto adjusts prices for splits and dividends
                        progress  = False          ) # progress bar

df_multi.columns  
df_multi['ETERNAL.NS'].head()
df_multi['HAL.NS']              # [1122 rows x 5 columns]


df_multi['HAL.NS']['Close']
df_multi[ ( 'HAL.NS', 'Close' ) ] # same as df_multi['HAL.NS']['Close']

df_multi.columns # MultiIndex([('ADANIGREEN.NS',   'Open'), ('ADANIGREEN.NS',   'High'),....
         


###############################################################################
# pandas.DataFrame.sort_values - Sort by the values along either axis.
# try sort

df.sort_values(by, # *,    # Name or list of names to sort by.
            # if axis is 0 or ‘index’ then may contain index levels and/or column labels
            # if axis is 1 or ‘columns’ then may contain column levels and/or index labels.
                     axis=0,   # “{0 or ‘index’, 1 or ‘columns’}”, default 0
                     ascending=True, 
                     inplace=False, 
                     kind='quicksort', # {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’},
                     na_position='last', 
                     ignore_index=False, 
                     key=None)

df_multi
df_multi.sort_values(by="Close", ascending=False, na_position="first")
df_multi.sort_values(by="50MA",  ascending=False, na_position="last", ignore_index=True )

# Customised , on converted lower case 
df_multi.sort_values(by="Symbol", ascending=False, key=lambda col: col.str.lower())

###############################################################################




### Updating yfinance’s multi-index structure to use row indexes #
#  as easy to use Pandas’ groupby operations for per-ticker calculations and  Technical indicators and visualizations become much simpler to implement as per 
# https://pythonfintech.com/articles/rethinking-yfinance-default-multiindex-format/

# clone the original dataframe
df_multi = df_multi.copy()
df_multi
# restructure the default multi-index yfinance dataframe by converting from
# wide to long format, renaming the indices, ensuring the columns are provided
# in OHLCV order, reordering the index such that date is first and symbol is
# second, and finally sorting the index itself
df_multi = df_multi.stack(level="Ticker", future_stack=True) # wide to long format
df_multi.index.names = ["Date", "Symbol"] # renames the index levels for clarity
df_multi = df_multi[["Open", "High", "Low", "Close", "Volume"]] # columns in standard OHLCV order
df_multi = df_multi.swaplevel(0, 1)  # reorders index so that Symbol comes first, then Date
df_multi = df_multi.sort_index()     # sorts the index for efficient access

df_multi.head(25)

df_multi.index
df_multi.columns
# display *just* the subset of AAPL market data
df_multi.xs("ABB.NS")

# The real power of this structure becomes apparent when we start doing analysis.
# notice how easy it is to analyze OHLCV data for each of the symbols with
# this structure by (1) first grouping on the symbol, followed by (2) applying
# our analysis method via 'transform'
df_multi["50MA"] = df_multi.groupby(level="Symbol")["Close"].transform(
    lambda x: x.rolling(window=50).mean()      )
df_multi

# group df_multi by Symbol, creating separate groups for each ticker
# select just the Close price column for all tickers
# apply the transform method to compute a 50-day moving average for each group in new column
# let's investigate the computed 50MA for AAPL
df_multi.xs("ABB.NS")["50MA"]

# now, let's *manually* compute the 50MA for AAPL (i.e., on a series rather
# than a multi-index dataframe)
df_multi.xs("ABB.NS")["Close"].rolling(window=50).mean()
# verify our calculations match
pd.testing.assert_series_equal(
    df_multi.xs("ABB.NS")["50MA"],
    df_multi.xs("ABB.NS")["Close"].rolling(window=50).mean(),
    check_names=False  )
# No error means the values are identical, so our calculation indeed correct.






stock_symbol  =  'ETERNAL.NS'
mystock       =  yf.Ticker(stock_symbol) 
mystock
info = mystock.info

hist = mystock.history(period="max") # history ' OHLCV + 'Dividends', + 'Stock Splits'
hist                                 # [10163 rows x 7 columns]
dir(hist)

type(hist)


df      = pd.DataFrame(hist["Close"])

returns = df.pct_change()

returns
returns.plot()


# asset_returns = returns
# type((asset_returns))
# returns = pd.Series(asset_returns)
# returns

# Sharpe Ratio = (Asset Return - Risk-Free Return) / Standard Deviation of Asset Return

rf_rate = 0.07 # risk-free rate  assuming 7%
sharpe = (  returns.mean() - rf_rate  ) / returns.std() * sqrt(252) # Annualize 
sharpe



# Beta measures asset volatility compared to overall market. < 1 less volatile, > more volatile
# Beta = Covariance(Asset Return, Market Return) / Variance(Market Return)



'''
# Fetch NIFTY 500 data
# nifty500_data = yf.download("^NSEI", start="YYYY-MM-DD", end="YYYY-MM-DD")
# ^NSMIDCP, ^CNXIT, ^CNX100, ^CNXPHARMA, ^CRSLDX  # No  '.NS' 
# S&P BSE SENSEX (^BSESN), NIFTY 50 (^NSEI)
# ^GSPC (SP500), Russell 2000 Index (^RUT), NASDAQ Composite (^IXIC), 
# NASDAQ-100 index (^NDX), the S&P 500 (^GSPC),
# Dow Jones Industrial Average (^DJI)
# Gold Aug 26 (GC=F)
# Bitcoin USD Price (BTC-USD)
# Crude Oil Aug 26 (CL=F)
# CBOE Volatility Index (^VIX)
# SSE Composite Index (000001.SS) Shanghai china, HANG SENG INDEX (^HSI)
# EURO STOXX 50 I (^STOXX50E), Euronext 100 Index (^N100)
# MOEX Russia Index (IMOEX.ME) # not available now
# FTSE Bursa Malaysia KLCI (^KLSE)
# KOSPI Composite Index (^KS11), IPC MEXICO (^MXX), 


'''

NSE500_data      =  yf.download('^NSEI' , period="max")
NSE500_data
NSE500_data['Close'].plot()

NSE500dl_returns = yf.download('^CRSLDX', period="max")
NSE500dl_returns
NSE500dl_returns['Close'].plot()

gold_returns     = yf.download('GC=F'   , period="max")
gold_returns
gold_returns['Close'].plot()

crude_returns   = yf.download('CL=F'    , period="max")
crude_returns
crude_returns['Close'].plot()

bcoin_returns   = yf.download('BTC-USD' , period="max")
bcoin_returns
bcoin_returns['Close'].plot()



mkt_returns ???
mkt_returns = 
NSE500_data['Close']
NSE500_data['Close'].iloc[0]
NSE500_data['Close'].iloc[-1]



mkt_returns = pd.Series(mkt_returns)  
mkt_returns= 0.12
beta = asset_returns.cov(mkt_returns) / mkt_returns.var()


# Technical Analysis with Bollinger Bands and RSI
# Bollinger Bands plot bands around a moving average, showing price volatility.
# RSI recent price performance on  0 to 100 scale.   < 30 is oversold ; > 70 is overbought.
# TA-Lib provide ready-made indicators


# DataCamp's Financial Analysis with Python Certification
# Udemy's Machine Learning for Finance with Python Course
# EdX's Python for Data Science, AI & Development Certification
# learn:  web scraping advanced financial data sets
#    Learning quantitative and statistical analysis libraries like SciPy
#    Studying predictive modeling techniques for financial forecasting
#    Implementing Python for tasks like derivative valuation and risk management


df_multi  # NSE500 OHLV data for 
?? df_multi['Close']
df_multi['ABB.NS']['Close']
df_multi[tickers]["Close"]

 
#  Multiple stocks data 

df_multi



# Plot data ###################################################################

import matplotlib.pyplot as plt


x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]
data = [x,y]
fig, ax = plt.subplots()

ax.plot(x, y, marker='o', label="Data Points")
ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

ax.legend() 
plt.show()



#plt.plot(x, y)
#plt.bar(x, y)            #     matplotlib.pyplot.bar(x, height)
#plt.hist(x, bins=10, color='steelblue')
#plt.scatter(x, y)
#plt.boxplot(data)
plt.imshow(data, cmap='viridis', interpolation='nearest')

plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()



plt.hist(x, bins=10, color='steelblue')
plt.scatter(x, y)

plt.plot(x, y)

'''
# Use plt.plot() to create the plot.
# Customize Plot: Add titles, labels and other elements using methods like plt.title(),  plt.xlabel() and plt.ylabel().
#Display Plot: Use plt.show() to display the plot.

'''


# Plot 
NSE500_data        =  yf.download('^NSEI', period="max")
ETERNAL_data       =  yf.download('ETERNAL.NS', period="max")
NH_data            =  yf.download('NH.NS', period="max")

ETERNAL_data

plt.figure(figsize=(10, 5))

sns.lineplot(data  =  NSE500_data["Close"]/NSE500_data["Close"].iloc[0],  linewidth = 2 , palette=['red']) # 
sns.lineplot(data  =  ETERNAL_data["Close"]/ETERNAL_data["Close"].iloc[0],  linewidth = 0.2 , palette=['green'] )
sns.lineplot(data  =  NH_data["Close"]/NH_data["Close"].iloc[0], linewidth = 0.2  )

# set the plot title
plt.title(  f"Stock Closing Prices ( "
           # f"{start_date.strftime('%Y-%m-%d')} "
           # f"to {end_date.strftime('%Y-%m-%d')})"   
           f"{start_date} to {end_date} )"     
          )
plt.xlabel("Date")                 # set the plot labels
plt.ylabel("Closing Price (Rs)")
plt.tight_layout()                 # finish constructing the plot
plt.show()


NSE500_data["Close"]['^NSEI']
NSE500_data["Close"].index


##### series plot NSE500_data["Close"]

sns.lineplot(x=NSE500_data["Close"].index, y=NSE500_data["Close"]['^NSEI'],\
             data=NSE500_data["Close"],  color="red", label='NSE500 Close Price')

    
# Label each point on the line
for x, y in zip(NSE500_data["Close"].index, NSE500_data["Close"]:  plt.text(x, y, f'{y}', fontsize=9, ha='right')

                

# seaborne
seaborn.set(style="darkgrid", context="notebook", palette="deep")
    # style: Background style — "white", "dark", "whitegrid", "darkgrid", "ticks".
    # context: Plot scaling — "paper", "notebook", "talk", "poster".
    # palette: Color theme — "deep", "muted", "bright", "pastel", "dark", "colorblind".
    # font (optional): Font family.
    # font_scale (optional): Font size scaling.
    # color_codes (optional): Enables shorthand colors from the palette.
    # rc (optional): Overrides default settings via a dictionary.

sns.lineplot(x, y, data=data, hue="column_name",  size="column_name", style='Column_name'
             err_style="band", hue="koi_score", palette="pastel")

###############################################################################
###############################################################################
# https://pythonfintech.com/articles/how-to-download-market-data-yfinance-python/
# Looping to plot all
# initialize a new figure
plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

# loop over the tickers
for ticker in NSE200_data():           # plot the closing price for each ticker in tickers
    sns.lineplot(   data  =  df_multi[ticker]["Close"],
                    label = ticker,
                    linewidth = 2                          )

# set the plot title
plt.title(  f"Stock Closing Prices ( "
           # f"{start_date.strftime('%Y-%m-%d')} "
           # f"to {end_date.strftime('%Y-%m-%d')})"   
           f"{start_date} to {end_date} )"     
          )
plt.xlabel("Date")                 # set the plot labels
plt.ylabel("Closing Price (Rs)")
plt.tight_layout()                 # finish constructing the plot
plt.show()




###############################################################################
###############################################################################

stock_symbol = 'ABB.NS'
# Fetch the historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the data
print(stock_data.head())

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='Close Price')
plt.title(f'Closing Prices of {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Close Price USD')
plt.legend()
plt.grid()
plt.show()

###############################################################################


###############################################################################

dat = yf.Ticker("KEI.NS")  # Narayan Hiridalaya

dat
dat.info
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')

dat.history(period='1mo').plot()


dat.option_chain(dat.options[0]).calls




# plots using seaborn

import seaborn as sns

tips = sns.load_dataset("tips")
tips

dir(sns)
# 'algorithms',
'load_dataset', 'reset_defaults','reset_orig','plotting_context',
'set','set_palette','set_style','set_theme','set_color_codes','set_context','set_hls_values',
'axes_style','axisgrid',
'palettes','blend_palette', 'diverging_palette',
'color_palette','crayon_palette', 'dark_palette', 'cubehelix_palette','colors','crayons',
'mpl', 'mpl_palette',


'barplot','boxenplot','boxplot','categorical', 'catplot',
'choose_colorbrewer_palette','choose_cubehelix_palette','choose_dark_palette',
'choose_diverging_palette','choose_light_palette', 'hls_palette','husl_palette',
'xkcd_palette', 'xkcd_rgb'
'clustermap',
'cm',

'countplot','displot', 'distplot','dogplot','ecdfplot',
'heatmap','histplot','light_palette',
'jointplot','kdeplot','lineplot','lmplot','miscplot','relplot',
'swarmplot','violinplot','stripplot','scatterplot','residplot','rugplot',

'utils','pairplot','pointplot','regplot','palplot',
'desaturate',
'despine',
'distributions', 'regression','relational',

'external',
'get_data_home','get_dataset_names',

'matrix',
'move_legend', 'rcmod','saturate','widgets',

tips

sns.stripplot( x= "day", y= "total_bill", df = "tips") #err

sns.countplot(x="total_bill", data=tips)

sns.barplot(x="day", y="total_bill", data=tips, palette="plasma")

sns.violinplot(x="day", y="total_bill", data=tips, hue="sex"    , split=True)

sns.boxplot(   x="day", y="total_bill", data=tips, hue="smoker"             )

sns.stripplot( x="day", y="total_bill", data=tips, hue="smoker", jitter=True, dodge=True)

sns.swarmplot( x="day", y="total_bill", data=tips)

plt.title("Plot of Total Bill by Day and Gender")
plt.show()





# %pip install scipy
import scipy
print(scipy.__version__)
#from scipy import stats
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mean_val = np.mean(data)
std_dev  = np.std(data)

t_stat, p_value = scipy.stats.ttest_1samp( data, popmean=5 )

print("t_stat:" , t_stat )
print("p_value:", p_value)


# integration

f = lambda y, x: x*y**2
i = scipy.integrate.dblquad( f,  0,  2,  lambda x: 0,  lambda x: 1 )
print(i)

# There is a lot more that SciPy is capable of, such as Fourier Transforms, Bessel Functions, etc.






# https://www.bseindia.com/download/BhavCopy/Equity/BhavCopy_BSE_CM_0_0_0_20250205_F_0000.CSV

# shorter stock test list for program testing purpose
def get_nifty50_symbols():  # simplified list, in practice, fetch this dynamically.
    return [ 'BAJFINANCE.NS',  'CHOLAFIN.NS', 'HINDUNILVR.NS',
             'WELCORP.NS', 'WELSPUNLIV.NS', 'WESTLIFE.NS', 'WHIRLPOOL.NS', 'ZFCVINDIA.NS',
             'ZENSARTECH.NS',  'ECLERX.NS']   # Add more symbols as needed

get_nifty50_symbols()

mystocks = pd.read_csv('/Users/gopalkumar/Documents/gkgit/mystocks/mystockdata1.csv')
mystocks['Symbol'] = mystocks['Ticker']
mystocks
list(mystocks['Symbol'])  # also ok
mystocks['Symbol'].values.tolist()  # same like above



def get_nifty50_symbols():
    mystocks = pd.read_csv('/Users/gopalkumar/Documents/gkgit/mystocks/mystockdata1.csv')
#    mystocks['Symbol'] = "'" + mystocks['Ticker'] + "'"
    mystocks['Symbol'] = mystocks['Ticker']

    return [mystocks['Symbol'].values.tolist()]
    #return [mystocks['Symbol'] ]

get_nifty50_symbols()






Trashdf = {}

stock = yf.Ticker("BAJFINANCE.NS")

stock
print(stock)
stock.info()

for symbol in get_nifty50_symbols():
#  print(symbol)
  try:  
    stock = yf.Ticker(symbol)
    # time delay for long list time.sleep(0.2÷≥l)
    Trashdf = Trashdf.append(stock)

  except Exception as e:
    print(f"Error processing getting data downlad of  {symbol}: {str(e)}")
#    return None



'''
# Function to fetch historical data
def get_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date, multi_level_index=False, auto_adjust=False)
## by setting multi_level_index and auto_adjust=False, we have negated recent changes in yfinance function


data = {} # Empty Data dictionary to hold stock data

# Fetch data for all tickers as stock_data and save in data{} dictionary
for ticker in tickers:
    try:
        stock_data = get_data(ticker, start_date, end_date)
        if len(stock_data) > 0:
            data[ticker] = stock_data
    except Exception as e:
        print(f"Error processing {symbol}: {str(e)}")
        return None


'''

# define calculate_metrics(symbol) to get summary stats of symbol

def calculate_metrics(symbol):
    stock = yf.Ticker(symbol)

    try:
        info = stock.info
        financials = stock.financials

        if 'marketCap' not in info:
            raise KeyError("Market Cap data not available")

        market_cap = info['marketCap']

        # Fetch historical data for the last year and 100 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        hist_data = stock.history(start=start_date, end=end_date)

        # Earnings Yield
        earnings = financials.loc['Net Income'].iloc[0] if 'Net Income' in financials.index else 0
        earnings_yield = (earnings / market_cap) * 100 if market_cap else 0

        # Dividend Yield
        dividend_yield = info.get('dividendYield', 0) * 100

        # 1-Year Volatility
        returns = hist_data['Close'].pct_change().dropna()
        volatility = returns.std() * np.sqrt(252) * 100  # Annualized volatility in percentage

        # 100-day EMA
        ema_100 = hist_data['Close'].ewm(span=100, adjust=False).mean().iloc[-1]
        current_price = hist_data['Close'].iloc[-1]

        # 1-year return
        one_year_return = (current_price / hist_data['Close'].iloc[0] - 1) * 100

        # 52-week high
        fifty_two_week_high = hist_data['Close'].max()

        # Check momentum criteria
        above_ema = current_price > ema_100
        sufficient_return = one_year_return >= 6.5
        near_high = current_price >= 0.75 * fifty_two_week_high

        meets_criteria = above_ema and sufficient_return and near_high

        return {
            'Symbol': symbol,
            'Earnings Yield (%)': earnings_yield,
            'Dividend Yield (%)': dividend_yield,
            'Volatility (%)': volatility,
            'Above 100-day EMA': above_ema,
            '1-Year Return (%)': one_year_return,
            'Within 25% of 52-week High': near_high,
            'Meets All Criteria': meets_criteria
        }
    except Exception as e:
        print(f"Error processing {symbol}: {str(e)}")
        return None




def main():   # just my stub to get table 
    nifty_symbols = get_nifty50_symbols()
    results = []

    for symbol in nifty_symbols:
        result = calculate_metrics(symbol)  # the data download function defined above by us
        if result:
            results.append(result)
        time.sleep(0.5)  # Introduce a 0.5 second delay after each symbol else too many reqests error.

    if not results:
        print("No valid data found for any symbols.")
        return

    # Create a DataFrame from the results
    df = pd.DataFrame(results)



main()


df
print(df)
results

###########################


def main():
    nifty_symbols = get_nifty50_symbols()
    results = []

    for symbol in nifty_symbols:
        result = calculate_metrics(symbol)  # the data download function defined above by us
        if result:
            results.append(result)
        time.sleep(0.5)  # Introduce a 0.5 second delay after each symbol else too many reqests error.

    if not results:
        print("No valid data found for any symbols.")
        return

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Filter stocks that meet all criteria
    df_filtered = df[df['Meets All Criteria']]

    if df_filtered.empty:
        print("No stocks meet all the momentum criteria.")
        return

    metric_columns = ['Earnings Yield (%)', 'Dividend Yield (%)', 'Volatility (%)']

    # Calculate ranks for each metric
    df_filtered['Earnings Yield Rank'] = df_filtered['Earnings Yield (%)'].rank(ascending=False, method='min')
    df_filtered['Dividend Yield Rank'] = df_filtered['Dividend Yield (%)'].rank(ascending=False, method='min')
    df_filtered['Volatility Rank'] = df_filtered['Volatility (%)'].rank(ascending=True, method='min')  # Lower volatility is better

    # Calculate weighted average rank
    df_filtered['Weighted Rank'] = (
        0.25 * df_filtered['Earnings Yield Rank'] +
        0.25 * df_filtered['Dividend Yield Rank'] +
        0.50 * df_filtered['Volatility Rank']
    )
# Calculate final rank based on weighted average rank
    df_filtered['Final Rank'] = df_filtered['Weighted Rank'].rank(method='min')

    # Sort by Final Rank
    df_filtered = df_filtered.sort_values('Final Rank')

    # Select columns to display
    display_columns = ['Symbol', 'Final Rank', 'Weighted Rank', 'Earnings Yield Rank', 'Dividend Yield Rank', 'Volatility Rank'] + \
                      metric_columns + ['1-Year Return (%)', 'Above 100-day EMA', 'Within 25% of 52-week High']

    # Display the results
    pd.set_option('display.float_format', '{:.2f}'.format)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df_filtered[display_columns].to_string(index=False))
    


    
if __name__ == "__main__":
      main()







###############################################################################

###############################################################################
###############################################################################

# Fuundamentals
import yfinance as yf

dir(yf)

['AsyncWebSocket', 'Auth', 'WebSocket', 'set_config', 'set_tz_cache_location','warnings'
 'cache', 'config',  'Calendars', 'calendars', 'utils',
 'ETFQuery', 'EquityQuery', 'FundQuery', 'PREDEFINED_SCREENER_QUERIES',
 'Industry',
 'Lookup','lookup', 'Search',  'search',

 'Market', 'MarketRegion',
 'Sector',
 
 'Ticker',  'Tickers','ticker', 'tickers',
 'download',

 'base',
 
 'const',
 'data',
 'domain',
 
 'enable_debug_mode',
 'exceptions',
 'live',
 'multi',
 'pricing_pb2',
 'scrapers', 'screen', 'screener', ]
 
 
 yf.config
# yf.config.network.proxy = "PROXY_SERVER"
# Cach - yfinance store some data locally: timezones /Users/<USER>/Library/Caches/py-yfinance:

# returns pandas.DataFrame with multi-level column names, with a level for ticker and price data

# new argument repair=True in history() and download() will attempt to fix a variety of price errors 

yf.Market('ASIA')# ['US', 'GB', 'ASIA', 'EUROPE', 'RATES', 'COMMODITIES', 'CURRENCIES', 'CRYPTOCURRENCIES']

yf.Market('ASIA').summary
yf.Market('EUROPE').summary # 


from datetime import datetime, timedelta

# Default init (today + 7 days)
calendar = yf.Calendars()

# Today's events: calendar of 1 day
tomorrow = datetime.now() + timedelta(days=1)
calendar = yf.Calendars(end=tomorrow)

# Default calendar queries - accessing the properties will fetch the data from YF
calendar.earnings_calendar
calendar.ipo_info_calendar
calendar.splits_calendar
calendar.economic_events_calendar

# Manual queries
calendar.get_earnings_calendar()
calendar.get_ipo_info_calendar()
calendar.get_splits_calendar()
calendar.get_economic_events_calendar()

# Earnings calendar custom filters
calendar.get_earnings_calendar(
    market_cap=10_000_000,  # filter out small-cap 
    filter_most_active=True,  # show only actively traded. Uses: `screen(query="MOST_ACTIVES")`
)

# Example of real use case:
# Get inminent unreported earnings events
today = datetime.now()
is_friday = today.weekday() == 4
day_after_tomorrow = today + timedelta(days=4 if is_friday else 2)

calendar = yf.Calendars(today, day_after_tomorrow)
df = calendar.get_earnings_calendar(limit=100)

unreported_df = df[df["Reported EPS"].isnull()]


'''
income_stmt, quarterly_income_stmt, ttm_income_stmt, get_income_stmt([as_dict, pretty, freq])
balance_sheet, get_balance_sheet([as_dict, pretty, freq])
cashflow, get_cashflow([as_dict, pretty, freq])

quarterly_cashflow, ttm_cashflow
get_earnings([as_dict, freq])
earnings
calendar : Returns a dictionary of events, earnings, and dividends for the ticker
get_earnings_dates([limit, offset])
earnings_dates
get_sec_filings()
sec_filings
'''

yf.Ticker('NH.NS').get_income_stmt(as_dict=False, pretty=False, freq='yearly') # [as_dict, pretty, freq])

yf.Ticker('NH.NS').income_stmt
yf.Ticker('NH.NS').income_stmt


yf.Ticker('NH.NS').income_stmt.columns
yf.Ticker('NH.NS').income_stmt.index
yf.Ticker('NH.NS').income_stmt.loc['Operating Revenue']
yf.Ticker('NH.NS').income_stmt.loc['Diluted EPS']

yf.Ticker('NH.NS').income_stmt

yf.Ticker('NH.NS').income_stmt.loc['Net Income']
yf.Ticker('NH.NS').income_stmt.loc['Selling And Marketing Expense']
yf.Ticker('NH.NS').income_stmt.loc['EBITDA']
yf.Ticker('NH.NS').income_stmt.loc['Total Revenue']


# Quarterly income

yf.Ticker('NH.NS').quarterly_income_stmt
yf.Ticker('NH.NS').quarterly_income_stmt.columns # DatetimeIndex(['2026-03-31', '2025-12-31', '2025-09-30', '2025-06-30', '2025-03-31'],  dtype='datetime64[ns]', freq=None)
yf.Ticker('NH.NS').quarterly_income_stmt.index

yf.Ticker('NH.NS').quarterly_income_stmt.loc['EBITDA']
yf.Ticker('NH.NS').quarterly_income_stmt


# Annual income 
yf.Ticker('NH.NS').ttm_income_stmt
#yf.Ticker('NH.NS').earnings # yf.Ticker('NH.NS').get_earnings()# [as_dict, freq])

yf.Ticker('NH.NS').earnings_dates # good
yf.Ticker('NH.NS').get_earnings_dates()#[limit, offset]) 

yf.Ticker('NH.NS').get_sec_filings() # Na for it
yf.Ticker('NH.NS').sec_filings       # empty for NH.NS


# Balance sheet

yf.Ticker('NH.NS').get_balance_sheet()#[as_dict=False, pretty=False, freq='yearly'])
yf.Ticker('NH.NS').balance_sheet

# Cash flow
yf.Ticker('NH.NS').cashflow
yf.Ticker('NH.NS').get_cashflow()#[as_dict, pretty, freq])
yf.Ticker('NH.NS').quarterly_cashflow # ??empty?
yf.Ticker('NH.NS').ttm_cashflow  # ok













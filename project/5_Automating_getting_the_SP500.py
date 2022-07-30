import bs4 as bs      #imports bueatifulSoup library
import pickle         #pickle serialzes any python object (saves objects/ variables)
import requests       #requests for api requests

def save_sp500_tickers():
  resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')      #request to wikipage containing list of S&P 500 companies 
  soup = bs.BeautifulSoup(resp.text, 'lxml')                                         #soup that comes from the response | (resp.txt) is the text from the response 
  table = soup.find('table', {'class': 'wikitable sortable'})               #gets table data with class of wikitable 
  # print(table.findAll('tr'))
  tickers = []

  for row in table.findAll('tr')[1:]:                  #for loop to iterate over the table | [1:] skips the first row of headers
    ticker = row.findAll('td')[0].text                  #gets all tiker symbols in the first column of the table    
    tickers.append(ticker)                              #appends ticker symbol to list 

  with open("sp500tickeres.pickle","wb") as f:          #saves the list in a file 
    pickle.dump(tickers,f)                              #dumps tickers to file f

  print(tickers)

  return tickers

save_sp500_tickers()
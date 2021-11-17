from bs4 import BeautifulSoup
import requests

liburl = "https://www.investing.com/indices/india-50-futures"
page = requests.get(liburl)

soup = BeautifulSoup(page.content, 'html.parser')
x = soup
div = x.find("span", {"data-test": "instrument-price-last"})
niftysgx = str(div.getText())
niftysgx = int(float(niftysgx.replace(',', '')))
print(niftysgx)

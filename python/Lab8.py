import requests, re
from bs4 import BeautifulSoup



data  =requests.get("https://www.nike.com/t/air-force-1-07-mens-shoes-5xqQ6q/DJ2739-100").text
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"headline-2 css-16cqcdq"})
title = span.text
span = soup.find("div", {"class":"product-price css-11s12ax is--current-price css-tpaepq"})
price = span.text
print("Item %s has price %s" % (title, price))



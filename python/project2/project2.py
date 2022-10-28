import requests, re
from bs4 import BeautifulSoup



data  =requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok").text
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("div", {"class":"product-card__title"})
title = span.text
span = soup.find("div", {"class":"product-card__product-count font-override__body1"})
colors = span.text
span = soup.find("div", {"class":"product-price is--current-price css-1ydfahe"})
price = span.text
print("Item %s has %s and price of %s" % (title, colors, price))


#info for shoe 1
#<div class="product-card__title" id="Nike Air VaporMax 2021 FK" role="link">Nike Air VaporMax 2021 FK</div>
#<div aria-label="Available in 9 Colors" class="product-card__product-count font-override__body1">9 Colors</div>
#<div aria-label="current price $131.97, original price $210" class="product-price__wrapper css-1q1feg0"><div aria-hidden="true" class="product-price is--current-price css-1ydfahe" data-test="product-price-reduced" role="link">$131.97</div><div aria-hidden="true" class="product-price us__styling is--striked-out css-0" data-test="product-price" role="link">$210</div></div>
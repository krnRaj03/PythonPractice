from cgitb import text
from bs4 import BeautifulSoup
import requests
import aspose.words as aw


# REDWOLF.IN
url="https://www.redwolf.in/iron-man-pattern-t-shirt-india"
result=requests.get(url)
doc=BeautifulSoup(result.text,"html.parser")


price=doc.find_all("span", class_="no_special_price_original_price")
for p in price:
  pname=p.text
  print(f"The price of the item is: {pname}")


#TRENDYOL

url1="https://www.trendyol.com/big-king/siyah-hakiki-deri-desenli-erkek-klasik-ayakkabi-p-52906979"
result1=requests.get(url1)
doc1=BeautifulSoup(result1.text,"html.parser")

price1=doc1.find_all("span", class_="prc-dsc")
for p1 in price1:
  pname1=p1.text
  print(f"The price of the item is: {pname1}")

#NIKE
url2="https://www.nike.com/t/air-jordan-1-mid-shoes-05CsKW/554724-371"
result2=requests.get(url2)
doc2=BeautifulSoup(result2.text,"html.parser")

price2=doc2.find_all("div", class_="product-price css-11s12ax is--current-price css-tpaepq")
for p2 in price2:
  pname2=p2.text
  print(pname2)
# for p2 in price2:
#   pname2=p2.text
#   print(f"The price of the item is: {pname2}")


url3="https://www.trendyol.com/erkek-t-shirt-x-g2-c73"
result3=requests.get(url3)
doc3=BeautifulSoup(result3.text,"html.parser")

price3=doc3.find_all("div", class_="prc-box-dscntd")

for p3 in price3:
  pname3=p3.text
  print([pname3])
#####
url4="https://www.trendyol.com/erkek-t-shirt-x-g2-c73"
result4=requests.get(url4)
doc4=BeautifulSoup(result4.text,"html.parser")

piks4=doc4.find_all("div", class_="image-overlay-body")

for p4 in piks4:
  pname4=p4.text
  print([pname4])

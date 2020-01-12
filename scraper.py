from urllib.request import urlopen as req

from bs4 import BeautifulSoup

# TODO: add functionality / method for multiple websites

WEBSITE = "https://www.revengeofficial.com/webstore"

client = req(WEBSITE)
html = client.read()
client.close()

# parsed html for the page
parsed_soup = BeautifulSoup(html, "html.parser")

# collection of products on the page
products = parsed_soup.findAll("div", {"class":"ProductList-item"})

# make sure the products have been found
print("Successfully found", len(products), "products.")

for product in products:
    print(product.h1.text, "- Price: $" + product.span.text)
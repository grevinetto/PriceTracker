from bs4 import BeautifulSoup
import requests

class PriceTracker:

    def __init__(self, product_url):
        self.product_url = product_url

    def get_price(self):
        response = requests.get(self.product_url, headers = {
            "User-Agent" : "MY_USER_AGENT",
            "Accept-Language" : "MY_ACCEPT_LANGUAGE"})
        self.soup = BeautifulSoup(response.text, "lxml")
        price_whole = self.soup.find(class_ = "a-price-whole").get_text().replace(",", ".")
        price_fraction = self.soup.find(class_ = "a-price-fraction").get_text()
        self.price_whole = float(price_whole + price_fraction)
        return self.price_whole

    def get_title(self):
        title = self.soup.find(id="productTitle").get_text().strip()
        return title

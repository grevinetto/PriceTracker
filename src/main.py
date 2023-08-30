from tracker import PriceTracker
from mailalert import MailAlert

TARGET_PRICE = 400 #PLACEHOLDER VALUE. YOU ESTABILISH


def main():
    url = "PRODUCT URL"
    test1 = PriceTracker(url)
    current_price = test1.get_price()
    title = test1.get_title()
    if current_price < TARGET_PRICE:
        MailAlert.send_email(current_price, title, url)

if __name__ == '__main__':
    main()
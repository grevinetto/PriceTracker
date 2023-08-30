# PriceTracker
A simple Python project that tracks the price of a given product on the Amazon website and sends e-mail alerts whenever the price goes down below an established threshold.

You will need to estabilish the threshold price and product url (on main.py) as well as some informations like your HTTP headers (on tracker.py), the sender and recipient emails, smtp address, port and your e-mail password (on mailalert.py). I recommend you use environment variables in order to keep your sensitive informations safe.

In the future, I'd like to add a little script that makes this code run on an estabilished frequency in order to keep tracking the price discounts, as well as a GUI to input the target price, url and other necessary data.

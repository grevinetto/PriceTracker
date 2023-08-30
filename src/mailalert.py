import smtplib

class MailAlert:

    @classmethod
    def send_email(self, price, title, url):
        sender_email = "MY_EMAIL"
        recipient_email = "MY_EMAIL"
        password = "MY_PASSWORD"
        smtp_address = "MY_SMTP_ADDRESS"
        port = "MY_PORT"
        message = f"{title} is now R${price}"

        with smtplib.SMTP(smtp_address, port=port) as connection:
            connection.starttls()
            result = connection.login(sender_email, password)
            connection.sendmail(
                from_addr = sender_email,
                to_addrs = recipient_email,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
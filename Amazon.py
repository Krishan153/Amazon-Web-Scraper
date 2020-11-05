import requests
from bs4 import BeautifulSoup
import smtplib

# Headers for request
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
 
# The webpage URL
URL = str(input('Please paste in the Amazon link: '))
 
# HTTP Request
webpage = requests.get(URL, headers=HEADERS)
 
# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "lxml")

# Function to get the title of the item
def get_title(soup):
    title = soup.find("span", attrs={"id":'productTitle'})
    title_value = title.string
    title_string = title_value.strip()
 
    return title_string
 
# Function to extract Product Price
def get_price(soup):
    price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    float_price = float(price[1:])
 
    return float_price


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('KrishansBot@gmail.com','idwiehhspukllpnb')
    subject = f'Your price for {get_title(soup)} just went down!'
    body = 'Your item dropped in price!'
    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'KrishansBot@gmail.com',
        'Bobbysteels7@gmail.com',
        message
    )

    print('Something is working')
    server.quit()

if get_price(soup) < 100:
    send_email()
else:
    print('something is broken')
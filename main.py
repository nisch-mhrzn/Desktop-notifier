import datetime
import time
import yfinance as yf

msft = yf.Ticker("MSFT")
data = msft.info
from plyer import notification

while True:
    notification.notify(
        title="MSFT Data".format(datetime.date.today()),
        message="Current Price ={cp}\nDayLow={dl} \nDayHigh={}".format(
            cp=data["currentPrice"],
            dl=data["regularMarketDayLow"],
            dh=data["regularMarketDayHigh"],
        ),
        app_icon="bell.ico",
        timeout=7,
    )

    time.sleep(60 * 60 * 2)

import datetime
import time
import yfinance as yf
from plyer import notification


def fetch_stock_data(ticker_symbol):
    """Fetches the latest stock data for the given ticker symbol."""
    ticker = yf.Ticker(ticker_symbol)
    try:
        data = ticker.info
        return {
            "currentPrice": data.get("currentPrice", "N/A"),
            "dayLow": data.get("regularMarketDayLow", "N/A"),
            "dayHigh": data.get("regularMarketDayHigh", "N/A"),
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def send_notification(stock_data, ticker_symbol):
    """Sends a desktop notification with stock data."""
    if stock_data:
        notification.notify(
            title=f"{ticker_symbol} Stock Update - {datetime.date.today()}",
            message=(
                f"Current Price: {stock_data['currentPrice']}\n"
                f"Day Low: {stock_data['dayLow']}\n"
                f"Day High: {stock_data['dayHigh']}\n"
                f"Last Updated: {datetime.datetime.now().strftime('%H:%M:%S')}"
            ),
            app_icon="bell.ico",
            timeout=7,
        )
    else:
        print("No stock data available for notification.")


def main():
    """Main function to run the stock notifier."""
    ticker_symbol = "MSFT"  # Replace with any stock ticker symbol
    interval = 60 * 60 * 2  # Notification interval in seconds (default: 2 hours)

    print(f"Starting stock notifier for {ticker_symbol}...")
    print(f"Notifications will be sent every {interval // 3600} hours.")

    try:
        while True:
            stock_data = fetch_stock_data(ticker_symbol)
            send_notification(stock_data, ticker_symbol)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stock notifier stopped by user.")


if __name__ == "__main__":
    main()

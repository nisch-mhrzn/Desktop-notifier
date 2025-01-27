# Stock Notifier

![Last Commit](https://img.shields.io/github/last-commit/nisch-mhrzn/Desktop-notifier)
![Repo Size](https://img.shields.io/github/repo-size/nisch-mhrzn/Desktop-notifier)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/github/license/nisch-mhrzn/stock-notifier)

This Python script sends periodic desktop notifications with the latest stock data for a specified ticker symbol using the `yfinance` and `plyer` libraries. It's designed to keep you updated on stock performance without requiring manual checks.

---

## Features

- **Dynamic Stock Data**: Fetches real-time stock data using the `yfinance` library.
- **Desktop Notifications**: Displays stock details like current price, day low, and day high.
- **Configurable Notification Interval**: Set how often you want to receive updates.
- **Graceful Exit**: Stop the script anytime with a keyboard interrupt.
- **Error Handling**: Handles network or API issues gracefully.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Required libraries:
  - `yfinance`
  - `plyer`

You can install the required libraries using:

```bash
pip install yfinance plyer
```

---

## Setup

1. Clone or download this repository to your local machine.
2. Ensure you have an icon file named `bell.ico` in the same directory as the script (optional, for notifications).
3. Open the script in a text editor and customize the following:
   - **Stock Ticker Symbol**: Replace `"MSFT"` in the `ticker_symbol` variable with your desired stock symbol.
   - **Notification Interval**: Adjust the `interval` variable (in seconds) to your preferred time interval.

---

## Usage

1. Run the script using the following command:

```bash
python main.py
```

2. The script will fetch and display stock data periodically, based on the configured interval.
3. Press `Ctrl + C` to stop the script at any time.

---

## Example Output

A sample notification message might look like this:

```
Title: MSFT Stock Update - 2025-01-27
Message:
Current Price: 300.25
Day Low: 295.50
Day High: 305.00
Last Updated: 14:35:12
```

---

## Customization

- **Notification Content**: Modify the `send_notification` function to include additional stock data or change the notification format.
- **Error Handling**: Add more specific error handling in the `fetch_stock_data` function if required.
- **Multi-Ticker Support**: Extend the script to handle multiple stock ticker symbols by iterating through a list.

---

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

---

## Contribution

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request or open an issue.

---




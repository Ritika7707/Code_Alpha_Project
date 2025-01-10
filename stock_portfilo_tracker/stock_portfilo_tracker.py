import yfinance as yf

portfolio = {}
 
def add_stock(symbol, quantity, purchase_price):
    """Add a stock to the portfolio."""
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['purchase_price'] = (
            portfolio[symbol]['purchase_price'] + purchase_price
        ) / 2
    else:
        portfolio[symbol] = {
            'quantity': quantity,
            'purchase_price': purchase_price,
        }
    print(f"Added {quantity} shares of {symbol} at ${purchase_price} each.")


def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from the portfolio.")
    else:
        print(f"{symbol} is not in the portfolio.")


def display_portfolio():
    """Display the portfolio with real-time data."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("Your Portfolio:")
    total_investment = 0
    total_value = 0

    for symbol, data in portfolio.items():
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")['Close'].iloc[-1]
        quantity = data['quantity']
        investment = quantity * data['purchase_price']
        current_value = quantity * current_price
        gain_loss = current_value - investment

        total_investment += investment
        total_value += current_value

        print(f"{symbol}:")
        print(f"  Quantity: {quantity}")
        print(f"  Purchase Price: ${data['purchase_price']:.2f}")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Gain/Loss: ${gain_loss:.2f}\n")

    print(f"Total Investment: ${total_investment:.2f}")
    print(f"Current Portfolio Value: ${total_value:.2f}")
    print(f"Overall Gain/Loss: ${total_value - total_investment:.2f}")


add_stock("AAPL", 10, 150)
add_stock("GOOGL", 5, 2800)
display_portfolio()
remove_stock("AAPL")
display_portfolio()
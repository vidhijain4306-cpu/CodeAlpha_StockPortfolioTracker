# CodeAlpha Internship - Task 2: Stock Portfolio Tracker
# Created by: Vidhi

import json
import os

PORTFOLIO_FILE = "portfolio.json"

# Default mock market prices for common stocks (can be customized by user)
MARKET_PRICES = {
    "AAPL": 180.50,
    "GOOGL": 140.20,
    "MSFT": 420.75,
    "AMZN": 175.10,
    "TSLA": 210.00,
    "NVDA": 890.30,
    "META": 490.60
}


def load_portfolio():
    """Loads saved portfolio from JSON file if available."""
    if os.path.exists(PORTFOLIO_FILE):
        try:
            with open(PORTFOLIO_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Corrupted portfolio file. Starting fresh.")
            return {}
    return {}


def save_portfolio(portfolio):
    """Saves the current portfolio data to a JSON file."""
    with open(PORTFOLIO_FILE, "w") as file:
        json.dump(portfolio, file, indent=4)
    print("Portfolio saved successfully.")


def get_current_price(symbol):
    """Gets market price from default list or prompts user for custom stock price."""
    if symbol in MARKET_PRICES:
        return MARKET_PRICES[symbol]
    
    print(f"Stock symbol '{symbol}' is not in predefined market list.")
    while True:
        try:
            price = float(input(f"Enter current market price for {symbol}: $"))
            if price > 0:
                return price
            print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid numeric value.")


def add_stock(portfolio):
    """Adds a new stock or increases quantity of existing stock."""
    print("\n--- ADD STOCK ---")
    symbol = input("Enter Stock Symbol (e.g. AAPL, TSLA, MSFT): ").strip().upper()
    
    if not symbol:
        print("Stock symbol cannot be empty.")
        return

    while True:
        try:
            quantity = int(input(f"Enter number of shares for {symbol}: "))
            if quantity > 0:
                break
            print("Quantity must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for shares.")

    while True:
        try:
            buy_price = float(input(f"Enter buy price per share for {symbol}: $"))
            if buy_price > 0:
                break
            print("Buy price must be greater than zero.")
        except ValueError:
            print("Please enter a valid numeric price.")

    if symbol in portfolio:
        # Update existing stock: calculate new weighted average price
        prev_qty = portfolio[symbol]["quantity"]
        prev_price = portfolio[symbol]["buy_price"]
        total_qty = prev_qty + quantity
        avg_price = ((prev_qty * prev_price) + (quantity * buy_price)) / total_qty
        
        portfolio[symbol]["quantity"] = total_qty
        portfolio[symbol]["buy_price"] = round(avg_price, 2)
        print(f"\nUpdated {symbol}: Total shares = {total_qty}, Avg Buy Price = ${avg_price:.2f}")
    else:
        portfolio[symbol] = {
            "quantity": quantity,
            "buy_price": buy_price
        }
        print(f"\nAdded {quantity} shares of {symbol} at ${buy_price:.2f} each.")

    save_portfolio(portfolio)


def remove_stock(portfolio):
    """Removes or reduces shares of a stock."""
    print("\n--- REMOVE STOCK ---")
    if not portfolio:
        print("Your portfolio is currently empty.")
        return

    symbol = input("Enter Stock Symbol to remove/sell: ").strip().upper()
    if symbol not in portfolio:
        print(f"'{symbol}' is not found in your portfolio.")
        return

    current_qty = portfolio[symbol]["quantity"]
    print(f"You currently hold {current_qty} shares of {symbol}.")

    while True:
        try:
            qty_to_remove = int(input(f"Enter shares to sell (1 to {current_qty}): "))
            if 0 < qty_to_remove <= current_qty:
                break
            print(f"Invalid quantity. Must be between 1 and {current_qty}.")
        except ValueError:
            print("Please enter a valid integer.")

    if qty_to_remove == current_qty:
        del portfolio[symbol]
        print(f"Sold all shares of {symbol}. Removed from portfolio.")
    else:
        portfolio[symbol]["quantity"] -= qty_to_remove
        print(f"Sold {qty_to_remove} shares. Remaining shares of {symbol}: {portfolio[symbol]['quantity']}")

    save_portfolio(portfolio)


def display_portfolio(portfolio):
    """Displays a detailed tabular summary of current portfolio holdings and performance."""
    print("\n" + "=" * 75)
    print("                      YOUR STOCK PORTFOLIO SUMMARY                     ")
    print("=" * 75)
    
    if not portfolio:
        print("Your portfolio is empty. Select option 2 to add stocks.")
        print("=" * 75)
        return

    header = f"{'Symbol':<8} {'Shares':<8} {'Buy Price':<12} {'Curr Price':<12} {'Invested':<12} {'Current Val':<12} {'P/L ($)':<10}"
    print(header)
    print("-" * 75)

    total_invested = 0.0
    total_current_value = 0.0

    for symbol, data in sorted(portfolio.items()):
        shares = data["quantity"]
        buy_price = data["buy_price"]
        current_price = get_current_price(symbol)

        invested_amt = shares * buy_price
        current_val = shares * current_price
        profit_loss = current_val - invested_amt

        total_invested += invested_amt
        total_current_value += current_val

        pl_str = f"+${profit_loss:.2f}" if profit_loss >= 0 else f"-${abs(profit_loss):.2f}"
        print(f"{symbol:<8} {shares:<8} ${buy_price:<11.2f} ${current_price:<11.2f} ${invested_amt:<11.2f} ${current_val:<11.2f} {pl_str:<10}")

    print("-" * 75)
    total_pl = total_current_value - total_invested
    total_pl_pct = (total_pl / total_invested * 100) if total_invested > 0 else 0.0

    print(f"Total Invested Capital : ${total_invested:.2f}")
    print(f"Total Current Value    : ${total_current_value:.2f}")
    
    if total_pl >= 0:
        print(f"Total Profit / Loss    : +${total_pl:.2f} (+{total_pl_pct:.2f}%) [PROFIT]")
    else:
        print(f"Total Profit / Loss    : -${abs(total_pl):.2f} ({total_pl_pct:.2f}%) [LOSS]")
    print("=" * 75)


def main():
    portfolio = load_portfolio()
    
    while True:
        print("\n=== CodeAlpha Stock Portfolio Tracker ===")
        print("1. View Portfolio & Profit/Loss")
        print("2. Add / Buy Stock")
        print("3. Remove / Sell Stock")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            display_portfolio(portfolio)
        elif choice == "2":
            add_stock(portfolio)
        elif choice == "3":
            remove_stock(portfolio)
        elif choice == "4":
            print("\nThank you for using Stock Portfolio Tracker. Happy investing!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

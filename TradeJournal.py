# 1. Trade Number / ID
# Just to keep track (1, 2, 3, …)
# 2. Date
# When the trade was taken
# 3. Asset/Instrument
# Example: NIFTY, BTC, USD/INR, RELIANCE, etc.
# 4. Direction
# Buy / Sell
# 5. Entry Price
# 6. Exit Price
# 7. Quantity / Lot Size
# 8. Profit/Loss
# 9. Reason for Entry
# Technical setup, news, breakout, etc.
# 10. Mistakes or Notes
# What went right/wrong; how you felt; any 

date=input("Enter the date of the trade (YYYY-MM-DD): ")
pair=input("Enter the asset/pair (e.g., NIFTY, BTC, USD/INR): ")
direction=input("Enter the direction (Buy/Sell): ").upper()
entry_price=float(input("Enter the entry price: "))
exit_price=float(input("Enter the exit price: "))

if direction == "BUY":
    profit_loss = exit_price - entry_price
else:
    profit_loss = entry_price - exit_price

reason_for_entry=input("Enter the reason for entry: ")

with open("trade_journal.txt", "a") as file:
    file.write(f"Trade Date: {date}\n")
    file.write(f"Asset/Pair: {pair}\n")
    file.write(f"Direction: {direction}\n")
    file.write(f"Entry Price: {entry_price}\n")
    file.write(f"Exit Price: {exit_price}\n")
    file.write(f"Profit/Loss: {profit_loss:.2f}\n")
    file.write(f"Reason for Entry: {reason_for_entry}\n")
    file.write("-" * 40 + "\n")


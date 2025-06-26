from forex_python.converter import CurrencyRates

c=CurrencyRates()

try:
    amount = float(input("Enter the amount in your currency: "))
    from_currency = input("Enter the currency you are converting from (eg. USD, INR...)").upper()
    to_currency = input("Enter the currency you are converting to (eg. USD, INR...)").upper()
    converted_amount=c.convert(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
except Exception as e:  
    print(f"An error occurred: {e}")
    print("Please check the currency codes and try again.")
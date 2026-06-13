from currency_converter import CurrencyConverter

c = CurrencyConverter()

while True:
    try:
        amount = float(input("Amount: "))

        from_curr = input("From currency (USD, EUR, GBP...): ").upper()
        to_curr = input("To currency: ").upper()

        result = c.convert(amount, from_curr, to_curr)

        print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}\n")

    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter valid currency codes.\n")
        continue

    again = input("Continue? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break

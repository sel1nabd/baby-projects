import requests

UserAmount = float(input("Please enter the amount you wish to convert: "))
InitialCurrency = str(input("Please enter the currency code that has to be converted: ")).upper()
EndCurrency = str(input("Please enter the currency code to convert to: ")).upper()

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={UserAmount}&from={InitialCurrency}&to={EndCurrency}"
) # API


print(
    f"{UserAmount} {InitialCurrency} is {response.json()['rates'][EndCurrency]} {EndCurrency}"
)


#!/usr/bin/python
""" Currency converter (from USD to GHS) """

print("USD to any Currency Converter")

print(
  "List of available currencies: \n 1 -> NGN (Nigeria Naira)  \n 2 -> MKD (Macedonian Denar)  \n 3 -> GHS (Ghana Cedis)  \n 4 -> BIRR (Ethiopian Birr) \n 5 -> KSH (Kenyan Shilling) "
)

currency_dict = {
  "NGN": 700,
  "MKD": 58.02,
  "GHS": 13.9,
  "BIRR": 53.2,
  "KSH": 122.65
}

currency = "NGN"

curr_num = int(input("Choose your currency's number : "))

# checking for selected currency
if curr_num == 1:
  currency = "NGN"

elif curr_num == 2:
  currency = "MKD"

elif curr_num == 3:
  currency = "GHS"

elif curr_num == 4:
  currency = "BIRR"

elif curr_num == 5:
  currency = "KSH"

else:
  print(
    "Sorry, no currency exists with this number. Hence, the default 'NGN' will be used"
  )

# creating variables

amt_to_convert = float(input("How much do you want to convert: "))

#rate = 700
# rate = float(input("Current Exchane Rate:"))

rate = currency_dict[currency]

final_amount = round((amt_to_convert * rate), 2)

print(f"Value: {currency}{final_amount}")


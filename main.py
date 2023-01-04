#!/usr/bin/python

""" Currency converter (from USD to GHS) """

Print ("USD to any currency Converter")

Print("List of availablecurrencies: \n 1 -> NGN (NIgeria Naira Cedis)  \n 2 -> D  \n 3 -> GHS (Ghana Cedis)  4 ->BIRR  5 -> Ksh ")

currency_dict = {"NGN": 700  "D": 62.0 "GHS": 13.9 "BIRR" : 53.2,  "Ksh": 122.65}

currency = "NGN"

curr_num = int(input("Choose your currency's number : "))
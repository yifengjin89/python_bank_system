# 2/12/2020
# bank_system

'''
person
class Person
attribute: name, id, phone


card
class Card
attribute: cardId, cardPassword, money


atm
class atm
attribute: users
behavior: open account, search info, deposit, withdraw, transfer, change password, lock account, unlock account,
cancel account, re-make a card, exit

'''
import random
from atm import Atm
from card import Card
ATM = Atm()
# CARD = Card()
# print(CARD.card_id)
while True:
    ATM.atm_interface()
    print("Please Enter a number to do the operation:  ")
    operation = str(input())
    if operation == "1":
        ATM.open_account()

    elif operation == "2":
        ATM.balance_info()

    elif operation == "3":
        ATM.deposit()

    elif operation == "4":
        ATM.open_account()

    elif operation == "5":
        ATM.open_account()

    elif operation == "6":
        ATM.open_account()

    elif operation == "7":
        ATM.open_account()

    elif operation == "8":
        ATM.open_account()

    elif operation == "9":
        ATM.open_account()

    elif operation == "10":
        ATM.open_account()

    elif operation == "11":
        print("Thanks for using, see you next time")
        break

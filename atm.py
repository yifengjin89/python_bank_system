# 2/12/2020
# atm info

from card import Card
from user import User

import random

class Atm(object):

    def __init__(self):
        self.all_users = {}

    def atm_interface(self):
        print("***********************************************************************")
        print("*                      Welcome to Yj bank                             *")
        print("*                                                                     *")
        print("*              Please enter number to do the operation                *")
        print("*                                                                     *")
        print("*       open account   (1)                  balance info    (2)       *")
        print("*       deposit        (3)                  withdraw        (4)       *")
        print("*       transfer       (5)                  change password (6)       *")
        print("*       lock account   (7)                  unlock account  (8)       *")
        print("*       cancel account (9)                  remake a card   (10)      *")
        print("*                             exit (11)                               *")
        print("*                                                                     *")
        print("***********************************************************************")

    def open_account(self):
        # press (1)
        print("Open account")
        name = str(input("Please Enter Your Name: "))
        user_id_number = int(input("Please Enter Your ID Number, digit only: "))
        phone = int(input("Please Enter Your Phone Number, digit only: "))
        password = int(input("Please setting Your PassWord, digit only: "))
        if not self.check_password(password):
            return -1
        card_id = self.create_card()
        print("Your Card ID is: %s " % card_id)
        card_balance = 0
        card_info = Card(card_id, password, card_balance)
        user_info = User(name, user_id_number, phone, card_info)
        self.all_users[card_id] = user_info
        print("Open Account Successfully !!! Please Remember Your Card ID !!!")



    def check_password(self, real_password):
        for i in range(3):
            re_password = int(input("Please Re-Enter Your PassWord, digit only: "))
            if real_password == re_password:
                return True
            else:
                remain = 2 - i
                if remain < 1:
                    break
                print("PassWord does not match!!! and You have %s" % remain + " chance")
        print("Your PassWord does not match!!!, operation failed !!!")
        return False


    def create_card(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            if not self.all_users.get(str):
                return str


    def balance_info(self):
        print("Balance info")
        card_id = input("Please Enter Card ID: ")
        user = self.all_users.get(card_id)
        if not user:
            print("Card Id does not exist!!")
        else:
            password = int(input("Please Enter Your PassWord, digit only: "))
            self.check_password(user.card.card_password)
            print("Card Id: %s   Balance: %s" % (user.card.card_id, user.card.card_balance))

    def deposit(self):
        # press (3)
        print("Deposit")
        card_id = input("Please Enter Card ID: ")
        user = self.all_users.get(card_id)
        if not user:
            print("Card Id does not exist!!")
        else:
            password = int(input("Please Enter Your PassWord, digit only: "))
            self.check_password(user.card.card_password)
            Deposit = int(input("Enter The Amount You want to Deposit: "))
            if Deposit <= 0:
                print("You Deposit must be great than 0, Transaction cancelled ！")
                return -1
            user.card.card_balance += Deposit
            print("Deposit successful!")


    def withdraw(self):
        pass

    def transfer(self):
        pass

    def change_password(self):
        pass

    def lock_account(self):
        pass

    def unlock_account(self):
        pass

    def cancel_account(self):
        pass

    def remake_card(self):
        pass

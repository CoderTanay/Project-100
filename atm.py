cardNumber = input("Enter Card Number: ")
pin = input("Enter Your Pin: ")

if(cardNumber == "123456789101" and pin == "9876"):
    class atm(object):
        def __init__(self, CashWithdrawl, BalanceEnquiry, DepostMoney):
            self.CashWithdrawl = CashWithdrawl
            self.BalanceEnquiry = BalanceEnquiry
            self.DepositMoney = DepostMoney
        def start(self):
            print("ATM ON")
        def loading(self):
            print("ATM LOADING...")
        def stop(self):
            print("ATM OFF")
ATM = atm('PRINTING MONEY', 'TWO MILLION DOLLARS', 'INSERT MONEY')
ATM.start()
print("Withdraw Cash")
ATM.loading()
print(ATM.CashWithdrawl)
print("Check Balance")
ATM.loading()
print(ATM.BalanceEnquiry)
ATM.stop()
        
import os
import json
from create_account import Create_account as ca
from check_balance import Check_balance as cb

print("WELCOME")

print("How can I help you ?")

while True:

    option =input("1-Create Account  \n2-Check Balance \n3-Deposit Amount \n4-Withdraw Amount  \n5-Exit \nAnswer - ")

    if (option=='1'):
        print("Ok First fill the following form")
        if ca.Create_new_account()==True:
            print("Account Succesfully Created")
        else:
            print("Failed")
    elif (option=='2'):
       cb.check_acc_balance()
    
    elif (option=='3'):
        pass
 
    elif (option=='5'):        
        break

print("Thank For coming see you later...")

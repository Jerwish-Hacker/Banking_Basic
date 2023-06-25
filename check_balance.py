import os
import json

class Check_balance():
    def check_acc_balance():
        flag=False
        while True:
            which_account_name=input("Enter the Name of Account Holder")
            which_account_should_be_check=input("Enter the account number")
            f=open("customer_details.json")
            data=json.load(f)
            for i in data:
                try:               
                    print("Amount :"+i[str(which_account_should_be_check)]["balance"])
                    flag=True
                    Break=input("OK ??")
                    break
                except:
                    pass
            if (flag==False):
                print("Enter Correct Account Number Please")
            else:
                break

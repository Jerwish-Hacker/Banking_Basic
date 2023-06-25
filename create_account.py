import os
import json

class Create_account():
    def Create_new_account():
        c_name=input("Name :")
        c_address=input("Address:")
        c_account=input("Ac no :")
        c_phone_no=input("Phone number :")
        c_pan_card=input("Pan card No :")
        c_balance=input("Deposit Amount :")

        filename = 'customer_details.json'
        entry={c_account:{"name":c_name,"address":c_address,"phoneno":c_phone_no,"panno":c_pan_card,"balance":c_balance}}

        with open(filename, "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file,indent=4)
        return True
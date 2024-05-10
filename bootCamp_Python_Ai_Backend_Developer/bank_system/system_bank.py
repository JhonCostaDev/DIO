
user_balance = 2000

print(f"""
***************************
        Welcome to
        
        PYTHON BANK
        
 
***************************
""")

while True:
      user_option= input(f"""
      Type [1] to Cash Withdrawal
      Type [2] to Deposit
      Type [3] to Balance Inquiry
      Type [0] to Exit\n
""")
      if user_option == "1":
            balance_requested = float(input("What's the value: \n"))
            if balance_requested > user_balance:
                  print("You don't have sufficient balance")
                  continue
            print(f"Mount solicited {balance_requested}")
            print("You can get the value down!")

      if user_option == "0":
            break


print("Fim")



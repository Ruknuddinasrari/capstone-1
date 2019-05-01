from olx import *

accounts = {}
user_id=1
print("-"*50)
print("Welcome to Olx")


while True:
	print("Hey! What would you like to do today?\n\n\
		1. Create olxAccount\n\
		2. Check Transactions\n\
		3. sell\n\
		4. purchase\n\
		5. Exit\n")

	choice=int(input("Enter your option:"))

	if choice==1:
		account_name=input("Enter your name:")
		phone_no=input("Enter your number:")
		address=input("enter your address:")
		vehicleamount=input("enter amount of vehicle")


		accounts[user_id] = OlxManager(account_name,user_id,address,vehicleamount,phone_no)
		

		print(f"Account created successfully! Your user_id is{user_id}")

		user_id +=1

	elif choice==2:

		Transaction=accounts[user_id].Transaction_statement()
		print(Transaction)

	elif choice==3:
		i = eval(input("Enter user id :"))
		if i == accounts[user_id]: 
			vehicle=int(input("Enter the no. of vehicles to be sold"))
			accounts[user_id].selling(vehicle)

	elif choice==4:
		i = eval(input("Enter user id :"))
		if i == accounts[user_id]: 
			vehicle = int(input("enter no. of vehicles to be bought"))
			accounts[user_id].purchasing(vehicle)

	elif choice==5:
		 break



		

	
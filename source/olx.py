#parent class
class OlxManager:

	def __init__(self,account_name,user_id,address,vehiclesamount,phone_no):
		self.account_name=account_name
		self.user_id=user_id
		self.address=address
		self.vehiclesamount=vehiclesamount
		self.phone_no=phone_no
		self.transactions = []

	def selling(self,vehicleamount=0):
		self.vehicleamount -= vehicleamount
		transaction = ('-'+str(vehicleamount),self.vehicleamount)
		self.transactions.append(transaction)

	def purchasing(self,vehicleamount=0):
		self.vehicleamount += vehicleamount
		transaction = ('+'+str(vehicleamount),self.vehicleamount)
		self.transactions.append(transaction)



			


#child class 1
class TwoWheelermanager(OlxManager):
	def _init_(self,tyres,transaction):
		self.tyres=tyres
		self.transaction
		if tyres == 2:
			print("two wheeler selected")



# child class 2
class FourWheelermanager(OlxManager):
	def _init_(self,tyres,transaction):
		self.tyres=tyres
		self.transaction
		if tyres == 4:
			print("four wheeler selected")
			

	
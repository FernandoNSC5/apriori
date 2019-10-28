import connectPg as db
from apyori import apriori as ap

class Main():

	def __init__(self):
		print("[SYSTEM] Initializing agent software")
		self.database = db.Connect()

		############################################
		## Apriori usage var
		self.aprioriTransaction = []
		self.aprioriTransactionVarMount = ['coffee', 'bread', 'milk', 'beer']


	###################################################
	##
	##	Core Methods
	##
	###################################################
	def printAllInfo(self):
		print(self.database.selectAllWithoutPk())

	# Creating Apriori transaction array
	def aprioriTransactionMount(self):
		print("[APRIORI] Creating transaction array...")
		# Gets data from database 
		dataInfo = self.database.selectAllWithoutPk()
		
		# For each row on database
		for element in dataInfo:
			
			#Auxiliar vars
			_toInput = []
			_counter = 0
			
			#For each item in the row
			for item in element:
				if(item):
					_toInput.append(self.aprioriTransactionVarMount[_counter])
				_counter = _counter+1

			#Appends an empty array
			self.aprioriTransaction.append([])
			aprioriTam = len(self.aprioriTransaction)

			#As python appends a memory address, this for creates new elements
			for item in _toInput:
				self.aprioriTransaction[aprioriTam-1].append(item)
		print("[APRIORI] Array creation OK")

	#Processing apriori
	def aprioriProcess(self):
		return list(ap(self.aprioriTransaction))


m = Main()
m.aprioriTransactionMount()
print(m.aprioriProcess()[5])
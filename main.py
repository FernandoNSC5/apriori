import connectPg as db

class Main():

	def __init__(self):
		print("[SYSTEM] Initializing agent software")
		self.database = db.Connect()


	###################################################
	##
	##	Core Methods
	##
	###################################################
	def printAllInfo(self):
		print(self.database.selectAllWithoutPk())

m = Main()
m.printAllInfo()
class Querys():

	def __init__(self):
		print("[SQL] Querys are ready to go")
		self.querys = [
			"SELECT * FROM test_elements;"
		]

	def loadAllQuerys(self):
		return self.querys

	def loadSpecific(self, queryNumber):
		return self.querys[queryNumber]

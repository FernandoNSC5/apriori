import connect as conn

class Main():

	def __init__(self):
		print("[SYSTEM] Initializing")
		self._allData = conn.loadAllData()

	def getAllData():
		return self._allData

_m = Main()
print(_m.getAllData())
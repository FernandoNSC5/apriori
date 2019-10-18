import mysql.connector as conn
import querys as Q

class Connection():

	def __init__(self):
		print("[SYSTEM][BD] Trying base connection")
		
		self.mybd = conn.connect(
			host="localhost",
			user="root",
			passwd="",
			database="tcc"
		)

		print("[SYSTEM][BD] Creating cursor")

		self.cursor = self.mybd.cursor()

		print("[SYSTEM][BD] Loading querys")
		self._query = Q.Querys()

	def executeQuery(self, query):
		return self.cursor.execute(query)

	def loadAllData(self):
		print("Query to execute: " + self._query.loadSpecific(0))
		return self.cursor.execute(self._query.loadSpecific(0))

a = Connection()
print(a.loadAllData())
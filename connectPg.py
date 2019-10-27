import psycopg2 as pg

class Connect():

	def __init__(self):
		print("[SYSTEM] Initializing database connection")
		try:
			self.conn = pg.connect(dbname='test', user='postgres', password='oj1s43jhps')
			print("[SYSTEM] Creating cursor")
			self.cursor = self.conn.cursor()
			self.initAllQuerrys()
		except:
			print("[SYSTEM] Error trying to connect to database")

	def initAllQuerrys(self):
		print("[SQL] Creating querys")
		self.getAll = "SELECT * FROM test"
		self.getAllWithoutPk = "SELECT t.coffee, t.bread, t.milk, t.beer FROM test t"

	def selectAll(self):
		self.cursor.execute(self.getAllWithoutPk)
		self.response = self.cursor.fetchall()
		print(self.response)


C = Connect()
C.selectAll()
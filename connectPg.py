import psycopg2 as pg

class Connect():

	def __init__(self):
		print("[SYSTEM] Initializing database connection")
		self.initAllQuerrys()


	######################################################
	##
	##	Core Methods
	##
	######################################################
	def initConnection(self):
		try:
			self.conn = pg.connect(dbname='test', user='postgres', password='oj1s43jhps')
			self.cursor = self.conn.cursor()
		except:
			print("[SYSTEM] An error ocured while trying to connect to the database")
			self.cursor.close()
			self.conn.close()

	def initAllQuerrys(self):
		print("[SQL] Creating querys")
		self.getAll = "SELECT * FROM test"
		self.getAllWithoutPk = "SELECT t.coffee, t.bread, t.milk, t.beer FROM test t"


	#####################################################
	##
	##	SQL Methods
	##
	#####################################################
	def selectAllWithoutPk(self):
		try:
			self.initConnection()
			self.cursor.execute(self.getAllWithoutPk)
			return self.cursor.fetchall()
		except:
			print("[SYSTEM] selectAllWithoutPk - Failure")
			return -1
		finally:
			self.cursor.close()
			self.conn.close()

	def selectAll(self):
		try:
			self.cursor.execut(self.getAll)
			return self.cursor.fetchall()
		except:
			print("[SYSTEM] selectAll - Failure")
			return -1
		finally:
			self.cursor.close()
			self.conn.close()
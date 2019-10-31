import psycopg2 as pg

class Connect():

	def __init__(self):
		print("[SYSTEM] Initializing database connection")
		
		# Base UTILS variables
		self._BASE = "test" 
		self.initAllQuerrys()

		print("[SQL] Initialization complete")


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
		self.getAllWithoutPk = "SELECT t.coffee, t.bread, t.milk, t.beer FROM "+self._BASE+" t"
		self.setDataToBase = "INSERT INTO " + self._BASE + "(bread, coffee, milk, beer) VALUES ( "


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
			self.initConnection()
			self.cursor.execut(self.getAll)
			return self.cursor.fetchall()
		except:
			print("[SYSTEM] selectAll - Failure")
			return -1
		finally:
			self.cursor.close()
			self.conn.close()

	def insertIntoTable(self, bread, coffee, milk, beer):
		try:
			query = self.setDataToBase
			query = query + bread + ", "
			query = query + coffee + ", "
			query = query + milk + ", "
			query = query + beer + " "
			query = query + " )"

			print("New query")
			print(query)
			
			self.initConnection()
			self.cursor.execut(query)
			#return self.cursor.fetchall()
			return 1

		except:
			print("[SYSTEM] insertIntoTable - Failure")
			return -1
		finally:
			self.cursor.close()
			self.conn.close()
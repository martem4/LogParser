import MySQLdb

class LogToDb:
    def __init__(self, dbConfig):
        self.dbConfig = dbConfig
        self.db = None

    #def sendLogToDb(self, dbRecord):


    @staticmethod
    def connectToDb(self):
        db = MySQLdb.connect(self.dbConfig.url,
                             self.dbConfig.port,
                             self.dbConfig.user,
                             self.dbConfig.passw,
                             self.dbConfig.dbname
                             )
        db.cursor()

    @staticmethod
    def sendLog(self, line):
        query =
import MySQLdb

class LogToDb:
    def __init__(self, dbConfig, logConfig):
        self.dbConfig = dbConfig
        self.logConfig = logConfig
        self.db = None

    @staticmethod
    def connectToDb(self):
        db = MySQLdb.connect(self.dbConfig.url,
                             self.dbConfig.port,
                             self.dbConfig.user,
                             self.dbConfig.passw,
                             self.dbConfig.dbname
                             )

    @staticmethod
    def sendLog(self, line):
        query = "INSERT INTO `systemevents` (`ReceivedAt`, `DeviceReportedTime`" \
                ", `Facility`,`Priority`,	`FromHost`, `Message`," \ 
                "`InfoUnitID`, `SysLogTag`, `EventLogType`,`GenericFileName`, `SystemID`, `processid`, " \
                "`checksum`) VALUES (now(), now(), 9, 6, 'logserver', " \
                "'"+ line +"', 1,'"+ self.logConfig.name +"', NULL, NULL, NULL, '', 0);"





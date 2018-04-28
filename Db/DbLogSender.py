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
        db.cursor()

    @staticmethod
    def sendLog(self, line):
        query = "INSERT INTO `systemevents` (`ReceivedAt`, `DeviceReportedTime`" \
                ", `Facility`,`Priority`,	`FromHost`, `Message`, `NTSeverity`, `Importance`,`EventSource`," \
                " `EventUser`, `EventCategory`, `EventID`,`EventBinaryData`, `MaxAvailable`, `CurrUsage`, `MinUsage`," \
                "`MaxUsage`, `InfoUnitID`, `SysLogTag`, `EventLogType`,`GenericFileName`, `SystemID`, `processid`, " \
                "`checksum`) VALUES (now(), now(), 9, 6, 'logserver', " \
                "'"+ line +"', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1," \
                " '"+ self.logConfig.name +"', NULL, NULL, NULL, '', 0);"



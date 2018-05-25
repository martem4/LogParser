import MySQLdb


class DbLogSender:
    def __init__(self, dbConfig, logConfig):
        self.dbConfig = dbConfig
        self.logConfig = logConfig
        self.db = None

    def connectToDb(self):
        self.db = MySQLdb.connect(host=str(self.dbConfig.url),
                                  user=str(self.dbConfig.user),
                                  passwd=str(self.dbConfig.passw),
                                  db=str(self.dbConfig.dbname),
                                  charset='utf8'
                                  )

    def sendLog(self, line):
        query = "INSERT INTO `systemevents` (`ReceivedAt`, `DeviceReportedTime`" \
                ", `Facility`,`Priority`,	`FromHost`, `Message`," \
                "`InfoUnitID`, `SysLogTag`, `EventLogType`,`GenericFileName`, `SystemID`, `processid`, " \
                "`checksum`) VALUES (now(), now(), 2, 3, 'logserver', " \
                "'" + line + "', 1,'" + self.logConfig.name + "', NULL, NULL, NULL, '', 0);"
        if self.db is not None:
            cursor = self.db.cursor()
            cursor.execute(query)
            self.db.commit()

    def closeDb(self):
        if self.db is not None:
            self.db.close()

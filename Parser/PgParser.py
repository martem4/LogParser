import File.FileTail

class PgParser:

    def __init__(self, logConfig, dbConfig):
        self.logConfig = logConfig
        self.dbConfig = dbConfig

    def parse(self):
        tail = File.FileTail.FileTail(self.logConfig.filePath)
        for line in tail:
            print(line, end="")



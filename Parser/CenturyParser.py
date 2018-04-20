import re
import xml
from xml.sax.handler import ContentHandler
from File.FileTail import FileTail


class CenturyParser:
    def __init__(self, logConfig, dbConfig):
        self.logConfig = logConfig
        self.dbConfig = dbConfig
        self.msg = ""

    def parse(self):
        tail = FileTail(self.logConfig.filePath)
        isException = False
        errorMsg = ""
        for line in tail:
            if isException:
                if re.search('\d\d-\d\d-\d\d\d\d \d\d:\d\d:\d\d.\d\d\d *', line, re.IGNORECASE):
                    print(errorMsg)
                    print("-----------------------------------------------------------------------------------")
                    isException = False
                    errorMsg = ""
                else:
                    if not re.search('ERROR|exception', line, re.IGNORECASE):
                        errorMsg += line
            if re.search('ERROR|exception', line, re.IGNORECASE):
                isException = True
                errorMsg += line

    def checkEmptyLine(self, line):
        if not line.strip():
            return True
        else:
            return False

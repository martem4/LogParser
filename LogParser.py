import xml.etree.cElementTree as ET
import configparser
from Config.DbConfig import DbConfig
from Config.LogConfig import LogConfig
from Parser.Log4jParser import Log4jParser
from Parser.PgParser import PgParser


class LogParser:
    def __init__(self):
        self.XML_CONFIG = "config.xml"
        self.DB_CONFIG = "db.ini"
        self.logConfigs = []
        self.dbConfig = None

    def readXmlConfig(self):
        try:
            tree = ET.parse(self.XML_CONFIG)
            root = tree.getroot()

            for config in root:
                logConfig = LogConfig()
                for child_config in config:
                    logConfig.name = config.attrib['name']
                    if child_config.tag == 'logFilePath':
                        logConfig.filePath = child_config.text
                    elif child_config.tag == 'logType':
                        logConfig.type = child_config.text
                self.logConfigs.append(logConfig)
        except IOError:
            print(self.XML_CONFIG + " config file not found!")

    def readDbConfig(self):
        config = configparser.RawConfigParser()
        config.read(self.DB_CONFIG)
        self.dbConfig = DbConfig()
        self.dbConfig.url = config.get("db", "url")
        self.dbConfig.port = config.get("db", "port")
        self.dbConfig.user = config.get("db", "user")
        self.dbConfig.passw = config.get("db", "passw")

    def readConfigs(self):
        self.readXmlConfig()
        self.readDbConfig()

    def get_logConfigs(self):
        return self.logConfigs


if __name__ == '__main__':

    l = LogParser()
    l.readConfigs()

    parserList = []

    for logConfig in l.get_logConfigs():
        if logConfig.type == 'log4j':
            parserList.append(Log4jParser(logConfig, l.dbConfig))
        elif logConfig.type == 'pg':
            parserList.append(PgParser(logConfig, l.dbConfig))

   # parserList[0].parse()

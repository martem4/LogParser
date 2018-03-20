import re
import xml
from xml.sax.handler import ContentHandler
from File.FileTail import FileTail


class Log4jParser:
    def __init__(self, logConfig, dbConfig):
        self.logConfig = logConfig
        self.dbConfig = dbConfig
        self.msg = ""

    def parseXmlEvent(self, xmlString):
        log4jSaxParser = Log4jSaxParser()
        xml.sax.parseString(xmlString, log4jSaxParser)
        print(log4jSaxParser.logMap.get('msg'))
        print(log4jSaxParser.logMap.get('thr'))

    def parse(self):
        tail = FileTail(self.logConfig.filePath)
        xmlOpen = False
        xml = ""
        for line in tail:
            if re.search('^<log4j:event(.*)level="ERROR"(.*)', line, re.IGNORECASE):
                xmlOpen = True
            if re.search('(.*)</log4j:event>(.*)', line, re.IGNORECASE):
                xmlOpen = False
                xml += line
                self.parseXmlEvent(xml)
                xml = ""
            if xmlOpen:
                xml += line


class Log4jSaxParser(ContentHandler):
    def __init__(self):
        ContentHandler.__init__(self)
        self.logMap = {'msg': '', 'thr': ''}
        self.tag = ""

    def startElement(self, name, attrs):
        self.tag = name

    def characters(self, content):
        if self.tag == 'log4j:message':
            self.logMap['msg'] += content
        elif self.tag == 'log4j:throwable':
            self.logMap['thr'] += content

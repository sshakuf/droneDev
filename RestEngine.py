
commands = {}


def CreateHTML(inBody):
    return '<html><header><title>ESP8266</title></header><body> ' + inBody + '</body></html>'


def AddRestEndPoint(inCommand, inHandler, inGet=None, inSet=None):
    
    commands[inCommand] = {'default':inHandler, 'get':inGet, 'set':inSet}

def Gethandler(inCommand, action):
    if inCommand in commands:
        if commands[inCommand][action] == None:
            return commands[inCommand]['default']
        
        return commands[inCommand][action]
    return None


def createHeader(content, contectType='text', fileext='html'):
    header = ''
    header += 'HTTP/1.1 200 OK\r\n'
    # header += 'Date: ' + time.localtime(time.time())
    header += 'Content-Type: ' + contectType +'/' + fileext + '\r\n'
    header += 'Content-Length: ' + str(len(content)) + '\r\n'
    header += "Access-Control-Allow-Origin: * \r\n"
    header += '\r\n'
    return header

def CreateHeaderJson(content):
    return createHeader(content, contectType='application', fileext='json')


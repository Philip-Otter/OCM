## Copyright 2023 Philip Otter

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver


def loadSettings(settingName):
    with open('./settings.conf', 'r') as settings:
        for line in settings:
            if(("#" in line) == False):
                if(settingName in line):
                    importDirty = line
                    print("Dirty "+settingName+" import:\n"+importDirty+"\n")
                    importCleaned = importDirty.split(':')[1]
                    print("Cleaned "+settingName+" import:\n"+importCleaned+"\n")
    settings.close()
    return(importCleaned)


def load(path):
    html = ''
    with open(path, 'r') as main:
        for line in main:
            if(('<var id = "port"' in line)==True):
                importDirty = line
                importFace = importDirty.split("|")[0]
                importTail = importDirty.split("|")[1]
                newLine = importFace + loadSettings("Port") + importTail
                print("\nNew Line:\n"+newLine)
                html += newLine
            else:
                html += line
    main.close()
    return(html)



def headers(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()


def startServer(port):
    class handler(BaseHTTPRequestHandler):
        
        
        def do_GET(self):
            if(self.path != "/"):
                if(".js" in self.path):
                    newPath = "./HTMLSources"+self.path
                    print("Adjusted path:  "+newPath)
                    headers(self)
                    self.wfile.write(bytes(load(newPath), "utf-8"))
            else:
                headers(self)
                self.wfile.write(bytes(load('./HTMLSources/main.html'), "utf-8"))


        def do_POST(self):
            if(self.path == "/mainpage/load"):
                headers(self)
                self.wfile.write(bytes("load API", "utf-8"))


    server = HTTPServer(("localhost",port), handler)
    server.serve_forever()



def main():
    startServer(int(loadSettings("Port")))  # Menu

main()
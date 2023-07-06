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


def loadHTML():
    html = ''
    with open('./HTMLSources/main.html', 'r') as main:
        for line in main:
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
            headers(self)
            self.wfile.write(bytes(loadHTML(), "utf-8"))


        def do_POST(self):
            if(self.path == "/mainpage/load"):
                headers(self)
                self.wfile.write(bytes("load API", "utf-8"))


    server = HTTPServer(("localhost",port), handler)
    server.serve_forever()



def main():
    startServer(int(loadSettings("Port")))  # Menu

main()
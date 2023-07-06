## Copyright 2023 Philip Otter

from http.server import HTTPServer, CGIHTTPRequestHandler
import os


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


def startServer(port):
    os.chdir('.')
    server = HTTPServer(server_address=('127.0.0.1', port), RequestHandlerClass=CGIHTTPRequestHandler)
    server.serve_forever()


def main():
    startServer(int(loadSettings("Port")))  # Menu

main()
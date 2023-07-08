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
                    print("Cleaned "+settingName+" import:"+importCleaned+"\n")
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
                print("New Line:\n"+newLine)
                html += newLine
            elif(('<var id = "host"' in line)==True):
                importDirty = line
                importFace = importDirty.split("|")[0]
                importTail = importDirty.split("|")[1]
                newLine = importFace + loadSettings("Host") + importTail
                print("New Line:\n"+newLine)
                html += newLine
            else:
                html += line
    main.close()
    return(html)



def headers(self, type):
    if(type == "html"):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "OPTIONS, GET, POST")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Max-Age", "*")
        self.send_header("Content-type", "text/html")
        self.end_headers()
    elif(type == "image"):
        self.send_response(404)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "OPTIONS, GET, POST")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Max-Age", "*")
        self.send_header("Content-type", "image/x-icon")
        self.end_headers()
    elif(type == "js"):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "OPTIONS, GET, POST")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Max-Age", "*")
        self.send_header("Content-type", "javascript")
        self.end_headers()
    else:
        print("\nERROR:  WRONG HEADER TYPE VALUE PROVIDED WHEN GENERATING RESPONSE HEADERS\n")


def startServer(port,host):
    class handler(BaseHTTPRequestHandler):
        
        
        def do_GET(self):
            if(self.path != "/"):
                if(".js" in self.path):
                    newPath = "./HTMLSources"+self.path
                    print("Adjusted path:  "+newPath)
                    headers(self,"js")
                    self.wfile.write(bytes(load(newPath), "utf-8"))
                elif("favicon" in self.path):
                    #newPath = "./HTMLSources"+self.path
                    #print("Adjusted path:  "+newPath)
                    headers(self,"image")
                    
            else:
                headers(self,"html")
                self.wfile.write(bytes(load('./HTMLSources/main.html'), "utf-8"))


        def do_POST(self):
            print("POST Path:  "+self.path)
            if(self.path == "/"):
                headers(self,"html")
                self.wfile.write(bytes("load API", "utf-8"))

        def do_OPTIONS(self):
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "OPTIONS, GET, POST")
            self.send_header("Access-Control-Allow-Headers", "*")
            self.send_header("Access-Control-Max-Age", "*")
            self.end_headers()
            print("OPTIONS Method requested.")
            print("Request path was  "+self.path+"\n")

    print("Host Value:",host)
    print("Port Value:",port)
    server = HTTPServer(("localhost",port), handler)
    server.serve_forever()



def main():
    startServer(int(loadSettings("Port")), str(loadSettings("Host")))  # Menu

main()
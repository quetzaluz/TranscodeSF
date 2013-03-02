import SocketServer

class HttpRequestHandler(SocketServer.StreamRequestHandler):
    # FIXME: Implement this!
    def handle (self):
        #The following informs the server about client requests.
        self.data = self.rfile.readline().strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        #The following splits up client request data for parsing below.
        splitdata = str(self.data).split()
        #The following parses client request and sends pages or errors in response
        if splitdata == []:
            pass
        elif splitdata[0] == "GET":
            try:
                pageref = "." + splitdata[1]
                pagefile = open(pageref, "rb")
                if pageref[-3:] == "htm" or pageref[-3] == "tml": 
                    reply = "HTTP/1.1 200 OK\nContent-type: text/html\r\n\r\n"+ pagefile.read()
                elif pageref[-3:] == "css":
                    reply = "HTTP/1.1 200 OK\nContent-type: text/css\r\n\r\n" + pagefile.read()
                else:
                    reply = pagefile.read()
                self.request.sendall(reply)
            except:
                self.request.sendall("HTTP/1.1 404 Not Found\nContent-type: text/html\r\n\r\n<html> <body> <h4> ERROR 404: File Not Found</h4></body></html>")
        elif splitdata[0] != "GET":
            self.request.sendall('HTTP/1.1 501 Not Implemented\nContent-type: text/html\r\n\r\n<html><body><h4> ERROR 501: Not Implemented</h4></body></html>')
        else:
            self.request.sendall('HTTP/1.1 400 Bad Request\nContent-type: text/html\n<html><body><h4>ERROR 400: Bad Request \r\n\r\nContent-type: text/html\r\n\r\n</h4></body></html>')
        
if __name__ == "__main__":
    # localhost is the name for the computer you are currently on.
    # It's equivalent to the IP address 127.0.0.1.
    host, port = "localhost", 8000

    # This class attribute tells the SocketServer class that even if a
    # previous program is still using this socket (which may take a while
    # for your OS to clean up if your webserver dies unexpectedly due to
    # an exception), then to just go ahead and reuse it anyway rather than
    # complaining about that port currently being in use.
    SocketServer.TCPServer.allow_reuse_address = True

    # Create the server by passing the class (not an object!) that you
    # want the server to create to handle requests.
    server = SocketServer.TCPServer((host, port), HttpRequestHandler)

    print "Running a server on http://%s:%d" % (host, port)
    print "Hit Ctrl-C to quit the server"
    server.serve_forever()

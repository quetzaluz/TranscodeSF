import SocketServer

class HttpRequestHandler(SocketServer.StreamRequestHandler):
    # FIXME: Implement this!
    pass


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

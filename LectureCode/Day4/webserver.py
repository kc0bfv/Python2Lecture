#!/usr/bin/env python
"""
curl "http://localhost:8000/"
curl "http://localhost:8000/just_a_get_request"
curl "http://localhost:8000/send_some_post_data" -d "Secret data"
"""

from __future__ import print_function

import argparse
import BaseHTTPServer

class BadHTTPServer(BaseHTTPServer.HTTPServer):
    """An instance of this class sticks around for the life of the server"""

    def __init__(self, *args, **kwargs):
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)
        self.last_request = "No previous request"

class BadHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Instances of this spin up to handle each request"""

    """
    # We don't need to initialze this class with anything specific,
    # so by not defining init on it, init calls fall through to superclass
    def __init__(self, *args, **kwargs):
        pass
    """

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.server.last_request)

        self.server.last_request = "{}: {}".format(self.client_address, 
                self.path)

    def do_POST(self):
        indat = ""
        last_read = "blank"
        self.rfile._sock.settimeout(3)
        while "\r\n" not in indat and last_read:
            try:
                last_read = self.rfile.read(1)
            except:
                last_read = ""
            indat += last_read

        """
        What is this dumb while loop doing, with that settimeout?  There isn't
        an easy way to get the post data...  send.rfile is an input stream
        positioned at the start of the post data.  Calling read on it will
        cause a set number of bytes to be read.  Unlike other read and recv
        operations, though, if that number of bytes isn't available, it'll
        block waiting for them to be.
        One solution - parse the HTTP header to determine the amount of bytes
        the web client says it sent.  That's an exercise for the reader...
        You'd still want to set a timeout though, in case the web client lied.
        """

        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.server.last_request)

        self.server.last_request = "{}: {} - {}".format(self.client_address, 
                self.path, indat)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8000)
    args = parser.parse_args()

    print("Serving on port {}...".format(args.port))

    server = BadHTTPServer(("", args.port), BadHTTPRequestHandler)
    server.serve_forever()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :basehttpserver_ex2.py
#description     :Shows the usage of baseHTTPSserver module, enabling an http server on a given port
#author          : Maimer
#date            : 23.11.2019
#version         :1.0
#usage           : basehttpserver_ex2.py 
#notes           : if at the browser you use localhost:port/slashdot/ it redirects to slashdot
#                  if nothing is passed it redirects to goole
#                  if at the browser you use localhost:port/freshmeat/ it redirects to freshmeat
#python_version  :2.7.6  
#=======================================================================

"""
URL redirection example.
"""

import BaseHTTPServer
import time
import sys


HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 1507 # Maybe set this to 9000.
REDIRECTIONS = {"/slashdot/": "http://slashdot.org/",
                "/freshmeat/": "http://freshmeat.net/"}
LAST_RESORT = "http://google.com/"

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(301)
        s.send_header("Location", REDIRECTIONS.get(s.path, LAST_RESORT))
        s.end_headers()
    def do_GET(s):
        s.do_HEAD()

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RedirectHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
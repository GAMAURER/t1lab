import time
import http.server
import datetime
import hashlib
import os


HOST_NAME =  '192.168.1.10' #'127.0.0.1'      # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>".encode())
        s.wfile.write(os.popen('date').read().encode())
        s.wfile.write((("<p>uptime"+os.popen('uptime').read())+"</p>").encode())
        s.wfile.write(("<p> processo:"+str(os.popen('ps -a'))+"</p>").encode())
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>".encode() )#% s.path
        s.wfile.write("</body></html>".encode())

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(datetime.datetime.now())
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
 

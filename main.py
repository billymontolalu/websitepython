import http.server
from os import path
import socketserver

class MyWebsite(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = 'index.html'
        elif self.path == "/daftar":
            self.path = 'daftar.html'
        elif self.path == "/survey":
            self.path = 'survey.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = "{post}\n".format(post = post_data)
        with open("file.txt", "a") as f:
            f.write(data)
            f.close()
        self.path = "survey_success.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
handler = MyWebsite

PORT = 8082
my_server = socketserver.TCPServer(("", PORT), handler)

my_server.serve_forever()
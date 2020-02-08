from chartisan import Chartisan
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler

PORT = 9000


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(Chartisan.build().labels(['a', 'b', 'c']).dataset(
            'Sample 1', [1, 2, 3]).dataset('Sample 2', [4, 3, 1]).toJSON().encode('utf-8'))


with TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

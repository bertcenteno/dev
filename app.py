from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Jenkins + Docker!\n")

HTTPServer(("0.0.0.0", 8081), Handler).serve_forever()

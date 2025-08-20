
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": "30",
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "404 Not Found", "message": f"Endpoint '{self.path}' does not exist"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleRequest):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Running on 8000 ;)")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
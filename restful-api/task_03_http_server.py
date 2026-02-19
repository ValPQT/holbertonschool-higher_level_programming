#!/usr/bin/python3
"""Simple HTTP API using http.server"""

import http.server
import socketserver
import json
from urllib.parse import urlparse

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    """Set up a basic web server using the http.server module"""

    def do_GET(self):
        """Handle different types of HTTP requests (GET, POST, etc.)"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            """Serve JSON data in response to specific endpoints"""
        elif path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
            }).encode())

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            }).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    httpd.serve_forever()

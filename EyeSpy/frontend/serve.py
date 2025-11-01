import http.server
import socketserver
import webbrowser
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.realpath(__file__)), **kwargs)

print(f"Starting frontend server on http://localhost:{PORT}")
print("Make sure your backend is running on http://localhost:5000")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend available at: http://localhost:{PORT}")
    webbrowser.open(f'http://localhost:{PORT}')
    httpd.serve_forever()
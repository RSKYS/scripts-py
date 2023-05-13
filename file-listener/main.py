import http.server
import os
import random
import socket
import socketserver

def port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Auto-select a random available port
while True:
    PORT = random.randint(900, 40000)
    if not port_in_use(PORT):
        break

# Prompt user for the file location
while not os.path.exists(DIRECTORY := input("Enter the file path: ")):
    print("Invalid directory, try again?")

# Start the server
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()

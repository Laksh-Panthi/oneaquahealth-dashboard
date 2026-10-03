import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

# Ensure working directory is the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS so local fetches work seamlessly
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

local_ip = get_local_ip()

print("=" * 64)
print("💧 OneAquaHealth Citizen Science Surveillance Dashboard")
print(f"📡 Local URL:        http://localhost:{PORT}")
print(f"👥 Teammate URL:     http://{local_ip}:{PORT} (Same Wi-Fi/Network)")
print("🇪🇺 Horizon Europe Grant 101086521")
print("📁 Datasets loaded:  data/sites.json & data/seed-observations.json")
print("=" * 64)
print("Opening dashboard in your web browser...")

webbrowser.open(f"http://localhost:{PORT}")

try:
    with socketserver.TCPServer(("", PORT), CustomHTTPHandler) as httpd:
        print("Server running. Press Ctrl+C to terminate.")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    sys.exit(0)

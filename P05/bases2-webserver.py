from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080


BASE_PATH = Path("P05/html")


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"Request received: {self.path}")

        # 🔹 Página principal
        if self.path == "/" or self.path == "/index.html":
            file_path = BASE_PATH / "index.html"

        else:

            requested_file = self.path.lstrip("/")
            file_path = BASE_PATH / requested_file

        try:

            with open(file_path, "r") as f:
                body = f.read()
            self.send_response(200)

        except FileNotFoundError:

            error_file = BASE_PATH / "error.html"
            with open(error_file, "r") as f:
                body = f.read()
            self.send_response(404)


        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()


        self.wfile.write(body.encode())



server = HTTPServer((IP, PORT), MyHandler)

print(f"Server running at http://{IP}:{PORT}")


try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
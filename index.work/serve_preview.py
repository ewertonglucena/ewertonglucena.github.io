from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

DOCUMENT = Path(__file__).resolve().parent.parent / 'CV - Ewerton Gomes de Lucena 2026 - PT-BR EN-US.html'

class PreviewHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path not in ('/', '/index.html'):
            self.send_error(404)
            return
        content = DOCUMENT.read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(content)

ThreadingHTTPServer(('127.0.0.1', 8876), PreviewHandler).serve_forever()

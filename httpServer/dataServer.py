from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer
import websockets
import tracemalloc
import json
import io
import asyncio
from socketserver import ThreadingMixIn

class MyHandler(BaseHTTPRequestHandler):
    my_variable="Loading"
    pet="Loading"
    serial="Loading"
    serial2="Loading"
    
    def do_POST(self):
        content_length=int(self.headers['Content-Length'])
        post_data=self.rfile.read(content_length)
        data=json.loads(post_data.decode('utf-8'))
        
        #MyHandler.my_variable=data.get('value')
        
        if self.path == '/get_variable':
            MyHandler.my_variable=data.get('value')
        elif self.path == '/get_pet':
            MyHandler.pet = data.get('value')
        elif self.path == '/get_serial':
            MyHandler.serial = data.get('value')
        elif self.path == '/get_serial2':
            MyHandler.serial2 = data.get('value')
        
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.handle_request())
    
    def handle_request(self):
        tracemalloc.start()
        
        if self.path == '/get_variable':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            
            self.wfile.write(MyHandler.my_variable.encode())
            
        elif self.path == '/get_pet':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(MyHandler.pet.encode())
        elif self.path == '/get_serial':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(MyHandler.serial.encode())
        elif self.path == '/get_serial2':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(MyHandler.serial2.encode())
        else:
            super().do_GET()
            
if __name__ == '__main__':
    server_adress = ('', 5000)
    httpd = TCPServer(server_adress, MyHandler)
    print('Starting server on port 5000...')
    httpd.serve_forever()
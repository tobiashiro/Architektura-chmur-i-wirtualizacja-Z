#!/usr/bin/env python3
import http.server
import socketserver
import re
import os
import time
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
import json



#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        path = urlparse(self.path)
        query_params = parse_qs(path.query) 
        
        if path.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            if query_params.get('str', None):
                string_to_operate = query_params.get('str', None)[0]
                output_string =  '{"lowercase" : 1, "uppercase" : 4, "digits" : 2, "special" : 8}'
                x = json.loads(output_string)
                self.wfile.write(output_string.encode('utf-8'))
                

        
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()

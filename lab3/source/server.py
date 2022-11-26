#!/usr/bin/env python3
import http.server
import socketserver
import re
import os
import time
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
import re



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
                output_param = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special': 0}
                regex = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")
                for sign in string_to_operate:
                    if sign.islower():
                        output_param['lowercase'] += 1
                    elif sign.isupper():
                        output_param['uppercase'] += 1
                    elif sign.isdigit():
                        output_param['digits'] += 1
                    elif regex.search(sign):
                        output_param['special'] += 1
                self.wfile.write(str(output_param).encode('utf-8'))
                

        
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()

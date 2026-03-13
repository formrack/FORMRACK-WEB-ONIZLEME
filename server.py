#!/usr/bin/env python3
"""
Formrack 3D Model Server
Dynamically scans models/ folder and serves files via HTTP
"""

import os
import json
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class ModelsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # API endpoint for listing models
        if self.path == '/api/models':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            
            models = []
            models_dir = Path('models')
            
            print(f'[API] Scanning for models in: {models_dir.absolute()}', file=sys.stderr)
            
            if models_dir.exists():
                # Scan for all .glb and .gltf files
                glb_files = sorted(models_dir.glob('*.glb'))
                gltf_files = sorted(models_dir.glob('*.gltf'))
                all_files = glb_files + gltf_files
                
                print(f'[API] Found {len(all_files)} model files', file=sys.stderr)
                
                for idx, file in enumerate(all_files, 1):
                    models.append({
                        'id': idx,
                        'name': file.stem,
                        'filename': file.name,
                        'description': f'3D Model - {file.name}',
                        'size': file.stat().st_size
                    })
                    print(f'[API] Added: {file.name} ({file.stat().st_size} bytes)', file=sys.stderr)
            else:
                print('[API] Models directory does not exist', file=sys.stderr)
            
            response = json.dumps({'models': models, 'total': len(models)})
            self.wfile.write(response.encode('utf-8'))
            print(f'[API] Responded with {len(models)} models', file=sys.stderr)
            return
        
        # Standard file serving with CORS headers
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def end_headers(self):
        # CORS headers for cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging
        return super().log_message(format, *args)

if __name__ == '__main__':
    PORT = 8000
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or '.')
    
    server = HTTPServer(('0.0.0.0', PORT), ModelsHandler)
    print('Formrack 3D Model Server Started')
    print(f'Server URL: http://localhost:{PORT}')
    print(f'Serving from: {os.getcwd()}')
    print(f'Models folder: {os.path.abspath("models")}')
    print(f'API endpoint: http://localhost:{PORT}/api/models')
    print('\nWaiting for requests...')
    print(f'Press Ctrl+C to stop\n')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n✋ Server stopped.')
        server.server_close()

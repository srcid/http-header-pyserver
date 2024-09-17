import http.server
import socketserver

PORT = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Capture and print the request headers and other details
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Prepare response containing request details
        response = (
            f"Request Method: {self.command}\n"
            f"Path: {self.path}\n"
            f"Headers:\n{self.headers}"
        )
        
        # Send the response back to the client
        self.wfile.write(response.encode('utf-8'))
    
    def do_POST(self):
        # Read and print the body of the POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response = (
            f"Request Method: {self.command}\n"
            f"Path: {self.path}\n"
            f"Headers:\n{self.headers}\n"
            f"Body:\n{post_data}"
        )

        self.wfile.write(response.encode('utf-8'))

# Set up the server
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

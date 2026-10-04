from http.server import HTTPServer, BaseHTTPRequestHandler

CONTENT = """<!DOCTYPE html>
<html>
<head><title>TCP/IP Protocol Suite</title></head>
<body>
  <h2>Name: S.Sudiksha &nbsp; | &nbsp; Reg No: 26018589 </h2>
  <h1>TCP/IP Protocol Suite</h1>
  <ul>
    <li><b>Application:</b> HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, Telnet, SSH, SNMP</li>
    <li><b>Transport:</b> TCP, UDP</li>
    <li><b>Internet:</b> IP, ICMP, ARP, IGMP</li>
    <li><b>Network Access:</b> Ethernet, Wi-Fi, PPP</li>
  </ul>
</body>
</html>"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(CONTENT.encode())

print("Server running at http://127.0.0.1:8000")
HTTPServer(("127.0.0.1", 8000), MyHandler).serve_forever()
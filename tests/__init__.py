from http.server import SimpleHTTPRequestHandler
import socketserver
from webium.driver import close_driver

from threading import Thread

httpd = socketserver.TCPServer(('', 0), SimpleHTTPRequestHandler)
PORT = httpd.server_address[1]


def setup_package():
    print("serving at port", PORT)
    thread = Thread(target=lambda: httpd.serve_forever())
    thread.daemon = True
    thread.start()


def teardown_package():
    close_driver()


def get_url(suffix=''):
    return 'http://localhost:%s/tests/pages/%s' % (PORT, suffix)

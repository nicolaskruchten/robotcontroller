import os.path
import cherrypy
from cherrypy.lib.static import serve_file
import serial
import binascii

s = serial.Serial('/dev/tty.usbserial-A600dJlw', 9600)


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return serve_file(os.path.join(current_dir, 'index.html'))
        
    @cherrypy.expose
    def jquery(self):
        return serve_file(os.path.join(current_dir, 'jquery-1.4.2.min.js'))
        
    @cherrypy.expose
    def position(self, x=0, y=0):
        print x
        print y
        s.write(binascii.unhexlify("%02x" % int(x)))
        s.write(binascii.unhexlify("%02x" % int(y)))
        return "ok"    

current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy.server.socket_port = 8080
cherrypy.server.socket_host = '10.0.1.200'
cherrypy.quickstart(HelloWorld())


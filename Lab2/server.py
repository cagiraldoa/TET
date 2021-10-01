from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler


class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(self.path[1:].encode())

        command = self.path[1:].encode()
        
        #2self.wfile.write(command)
        try:
               
            if command == "X":
                self.wfile.write("X".encode())
                #break
            else:
                print("Ecuación:", command.decode("utf-8"))
                result = eval(command)
                self.wfile.write(str(result).encode())
        except (ZeroDivisionError):
            self.wfile.write("ZeroDiv".encode())
        except (ArithmeticError):
            self.wfile.write("MathError".encode())
        except (SyntaxError):
            self.wfile.write("SyntaxError".encode())
        except (NameError):
            self.wfile.write("NameError".encode())

def main():

    PORT = 8006
    server = HTTPServer(('', PORT), Servidor)
    print("Servidor corriendo en el puerto", PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()
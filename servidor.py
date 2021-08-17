import socket		 	 # Import socket module
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 # Create a socket object

host = "127.0.0.1"                   # Get local machine name
port = 9092


s.bind((host, port)) 			 # Bind to the port
s.listen(5) 			         # Now wait for client connection.

print("Servidor corriendo")

while True:
     c, addr = s.accept() 		# Establish connection with client.
     print('Conexión del cliente ', addr)

     while True:
          try:
               equation=c.recv(1024).decode()
               if equation == "X":
                    c.send("X".encode())
                    break
               else:
                    print("Ecuación:", equation)
                    result = eval(str(equation))
                    c.send(str(result).encode())
          except (ZeroDivisionError):
               c.send("ZeroDiv".encode())
          except (ArithmeticError):
               c.send("MathError".encode())
          except (SyntaxError):
               c.send("SyntaxError".encode())
          except (NameError):
               c.send("NameError".encode())

     c.close()
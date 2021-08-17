import socket		 	 # Import socket module
import sys
import ipaddress

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 # Create a socket object


host = "172.31.9.184"                    # Reading IP Address
port = 9085                           # Reading port number
s.connect((host, port))                           # Connecting to server
print("IP:", host)
print("PORT:", port)

while(True):
    equ=input("Calculadora Lab-01! \n - X Para salir \n - Ingrese los numeros y el operador para la operación\n ")
    s.send(equ.encode())
    result = s.recv(1024).decode()

    if result == "X":
        print("Conexión Terminada, Adios")
        break
    elif result == "ZeroDiv":
        print("No puedes dividir por cero")
    elif result == "MathError":
        print("Error Matematico")
    elif result == "SyntaxError":
        print("Error Sintatico")
    elif result == "NameError":
        print("Ingresa una ecuación")
    else:
        print("Resultado:", result)

s.close 				 # Close the socket when done
print('Conexión Terminada')
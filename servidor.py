import socket
import constants

#Create a socket...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Main function...
def main():
    print('***********************************')
    print('Servidor corriendo...')
    print('IP:',constants.SERVER_ADDRESS )
    print('PORT:', constants.PORT)
    create_server_socket()
    
# Function to start server process...
def create_server_socket():
    tuple_connection = (constants.SERVER_ADDRESS,constants.PORT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(tuple_connection)
    server_socket.listen(constants.BACKLOG)
    print('Socket escuchando...', server_socket.getsockname())        
        
    # Loop for waiting new connections...
    while True:
          client_connection, client_address = server_socket.accept()		
          print(f'Cliente nuevo. IP: {client_address[0]}.PORT: {client_address[1]}')

          while True:
               try:
                    equation=client_connection.recv(1024).decode()
                    if equation == "X":
                         client_connection.send("X".encode())
                         break
                    else:
                         print("Ecuación:", equation)
                         result = eval(str(equation))
                         client_connection.send(str(result).encode())
               except (ZeroDivisionError):
                    client_connection.send("ZeroDiv".encode())
               except (ArithmeticError):
                    client_connection.send("MathError".encode())
               except (SyntaxError):
                    client_connection.send("SyntaxError".encode())
               except (NameError):
                    client_connection.send("NameError".encode())

          print("Conexión Terminada")
          client_connection.close()


if __name__ == '__main__':
     main()
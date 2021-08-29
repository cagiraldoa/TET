import socket
import threading
import constants

#Create a socket...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER

# Main function...
def main():
    print('***********************************')
    print('Servidor corriendo...')
    print('IP:',server_address  )
    print('PORT:', constants.PORT)
    server_execution()
    

def handler_client_connection(client_connection,client_address):
     print(f'Nuevo cliente: {client_address[0]}:{client_address[1]}')
     is_connected = True
     while is_connected:
          data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
          remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
          remote_command = remote_string.split()
          command = remote_command[0]
          print (f'Cliente: {client_address[0]}:{client_address[1]}')
          print(command)

          
          try:
               
               if command == "X":
                    client_connection.send("X".encode())
                    break
               else:
                    print("Ecuación:", command)
                    result = eval(str(command))
                    client_connection.send(str(result).encode())
          except (ZeroDivisionError):
               client_connection.send("ZeroDiv".encode())
          except (ArithmeticError):
               client_connection.send("MathError".encode())
          except (SyntaxError):
               client_connection.send("SyntaxError".encode())
          except (NameError):
               client_connection.send("NameError".encode())

     print(f'Conexión con {client_address[0]}:{client_address[1]} terminada...')
     client_connection.close()

def server_execution():
     tuple_connection = (server_address,constants.PORT)
     server_socket.bind(tuple_connection)
     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     server_socket.listen(5)
     print('Socket esta escuchando...')
     while True:
          client_connection, client_address = server_socket.accept()
          client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
          client_thread.start()
     print('Socket is closed...')
     server_socket.close()


if __name__ == '__main__':
     main()
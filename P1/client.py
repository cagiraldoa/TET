import http.client

client = http.client.HTTPConnection('127.0.0.1', 8006)

while(True):

    print("\nBienvenido a nuestra Base de Datos Distribuida. Aqui podras guardar tus datos personales.\n")
    print("Todo sera muy sencillo para ti solo sigue las siguientes reglas:\n")
    print("Seguiremos el formato   <k,v>     <clave unica,(Nombre,Edad,Ciudad)>\n")
    print("Ejemplo--->  <cagiraldoa,(Cristian,19,Medellin)>\n")
    print("A para agregar\n")
    print("C para consulta de datos por <k>\n")
    print("X si no necesitas más de mi\n")

    decision=input("Que decides:   ")

    if(decision=="A"):
        equ=input("Ingresa tu <k,v>\n\n")

    if(decision=="C"):
        equ=input("Ingresa tu <k>\n\n")


    if(decision=="X"):
        break
    
    client = http.client.HTTPConnection('127.0.0.1', 8006)
    client.request("GET", f"/{decision}/{equ}") 

    
    
    #sol = client.getresponse()
    #answer = sol.read().decode("utf-8")
    #print(answer)

print("Bye!")
import http.client
import constants

client = http.client.HTTPConnection(constants.IP_SERVER, constants.PORT)

print("\nBienvenido a nuestra Base de Datos Distribuida. Aqui podras lo que desees.\n")
print("Todo sera muy sencillo para ti solo sigue las siguientes reglas:\n")
print("Seguiremos el formato   <k,v>     <clave unica, lo que desees>\n")
print("Ejemplo--->  <cagiraldoa, Hola Soy Cristian Giraldo>\n")

while(True):

    print("A para agregar")
    print("C para consulta de datos por <k>")
    print("B para borrar datos por <k>")
    print("M para modificar datos por <k>")
    print("X si no necesitas más de mi\n")

    decision=input("Que decides:   ")
    print()

    if(decision=="A" or decision=="a"):
        equ=input("Ingresa tu <k,v>  ")
        print()

    elif(decision=="C" or decision=="c"):
        equ=input("Ingresa tu <k>  ")
        print()
        client = http.client.HTTPConnection(constants.IP_SERVER, constants.PORT)
        client.request("GET", f"/{decision}/{equ}") 
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")
        
        if(answer==""):
            print("No hay registros")
            print()

        elif(answer!=""):
            print(answer)
            
             
            


    elif(decision=="B" or decision=="b"):
        equ=input("Ingresa tu <k>  ")
        print()
        client = http.client.HTTPConnection(constants.IP_SERVER, constants.PORT)
        client.request("GET", f"/{decision}/{equ}") 
    
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")


        if(answer!=""):
            print(answer)
            print()
            equ=input("Escoge el identificador [#]   ")

            decision = "D"

        elif(answer==""):
            print("No hay registros")
            print()
            

    
    elif(decision=="M" or decision=="m"):
        equ=input("Ingresa tu <k>  ")
        print()
        client = http.client.HTTPConnection(constants.IP_SERVER, constants.PORT)
        client.request("GET", f"/{decision}/{equ}") 
    
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")

        if(answer!=""):
            print(answer)
            print()
            equ = []
            equ.append(input("Escoge el identificador [#]   "))
            equ.append(input("Ingresa  (v)   "))

            decision = "U"

        if(answer==""):
            print("No hay registros")
            print()

        

    elif(decision=="X" or decision=="x"):
        break


    else:
        print("Tienes opciones claras. Decidete por una correcta\n")
        continue
        
    
    
    if(decision!="C" and decision!="c"):
        client = http.client.HTTPConnection(constants.IP_SERVER, constants.PORT)
        client.request("GET", f"/{decision}/{equ}".replace(" ","+").replace('\'',"")) 

        
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")
        print(answer)

print("Bye!")
import http.client

client = http.client.HTTPConnection('127.0.0.1', 8007)

print("\nBienvenido a nuestra Base de Datos Distribuida. Aqui podras guardar tus datos personales.\n")
print("Todo sera muy sencillo para ti solo sigue las siguientes reglas:\n")
print("Seguiremos el formato   <k,v>     <clave unica,(Nombre,Edad,Ciudad)>\n")
print("Ejemplo--->  <cagiraldoa,(Cristian,19,Medellin)>\n")

while(True):

    print("A para agregar")
    print("C para consulta de datos por <k>")
    print("B para borrar datos por <k>")
    print("M para modificar datos por <k>")
    print("X si no necesitas más de mi\n")

    decision=input("Que decides:   ")
    print()

    if(decision=="A"):
        equ=input("Ingresa tu <k,v>  ")
        print()

    elif(decision=="C"):
        equ=input("Ingresa tu <k>  ")
        print()

    elif(decision=="B"):
        equ=input("Ingresa tu <k>  ")
        print()
        client = http.client.HTTPConnection('127.0.0.1', 8007)
        client.request("GET", f"/{decision}/{equ}") 
    
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")
        print(answer)
        print()
        equ=input("Escoge el identificador [#]   ")

        decision = "D"

    
    elif(decision=="M"):
        equ=input("Ingresa tu <k>  ")
        print()
        client = http.client.HTTPConnection('127.0.0.1', 8007)
        client.request("GET", f"/{decision}/{equ}") 
    
        sol = client.getresponse()
        answer = sol.read().decode("utf-8")
        print(answer)
        print()
        equ = []
        equ.append(input("Escoge el identificador [#]   "))
        equ.append(input("Ingresa  (v)    (Nombre,Edad,Ciudad)   "))

        decision = "U"

        

    elif(decision=="X"):
        break
    
    client = http.client.HTTPConnection('127.0.0.1', 8007)
    client.request("GET", f"/{decision}/{equ}".replace(" ","").replace('\'',"")) 

    
    sol = client.getresponse()
    answer = sol.read().decode("utf-8")
    print(answer)

print("Bye!")
import http.client



client = http.client.HTTPConnection('172.31.9.184', 8003)

while(True):

    equ=input("Calculadora Lab-01! \n - X para salir\n - Ingrese los numeros y el operador para la operación\n ")

    if(equ=="X"):
        break
    client.request("GET", f'/{equ}') 
    sol = client.getresponse()
    answer = sol.read().decode("utf-8")
    print(answer)

print("Bye!")
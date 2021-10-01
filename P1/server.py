from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import pandas as pd

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(self.path[1:].encode())

        user = str(self.path[1:]).split("/")
        print (user)
        
        #2self.wfile.write(command)
        
               
        if user[0] == "X":
            self.wfile.write("X".encode())
            #break
        elif user[0] == "A":
            user_m = user[1].replace("<","").replace(">","").replace("(","").replace(")","").replace(" ","")

            user_m2 = user_m.split(",")

            data_name = pd.read_csv('Name.csv')
            data_age = pd.read_csv('Age.csv')
            data_city = pd.read_csv('City.csv')

            data_name = data_name.append({'Key' : user_m2[0], 'Name' : user_m2[1], 'Num' : len(data_name.index)}, ignore_index=True)
            data_name = data_name.to_csv('Name.csv', index=False)

            data_age = data_age.append({'Key' : user_m2[0], 'Age' : user_m2[2], 'Num' : len(data_age.index)}, ignore_index=True)
            data_age = data_age.to_csv('Age.csv', index=False)

            data_city = data_city.append({'Key' : user_m2[0], 'City' : user_m2[3], 'Num' : len(data_city.index)}, ignore_index=True)
            data_city = data_city.to_csv('City.csv', index=False)

        elif user[0] == "C":
            user_m = user[1].replace("<","").replace(">","").replace("(","").replace(")","").replace(" ","")
            print(user_m)
            #user_m2 = user_m.split(",")

            data_name = pd.read_csv('Name.csv')
            data_age = pd.read_csv('Age.csv')
            data_city = pd.read_csv('City.csv')

           
            for i in data_name.index:
                for j in data_age.index:
                    for k in data_city.index:
                        if(data_name['Key'][i]==data_age['Key'][j] and data_name['Key'][i]==data_city['Key'][k] 
                        and data_name['Key'][i]==user_m
                        and data_name['Key'][i]==data_city['Key'][k] and data_city['Key'][k]==data_age['Key'][j] and
                        data_name['Num'][i]==data_age['Num'][j] and data_name['Num'][i]==data_city['Num'][k]
                        and data_name['Num'][i]==data_city['Num'][k] and data_city['Num'][k]==data_age['Num'][j]):
                            
                            valores = "<",data_name['Key'][i],",(",data_name['Name'][i],",",data_age['Age'][j],",",data_city['Num'][k],")>"

                            print(f"<{data_name['Key'][i]},({data_name['Name'][i]},{data_age['Age'][j]},{data_city['Num'][k]})>")
       

def main():

    PORT = 8006
    server = HTTPServer(('', PORT), Servidor)
    print("Servidor corriendo en el puerto", PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()
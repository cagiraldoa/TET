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
        
        try:      
            if user[0] == "X":
                self.wfile.write("X".encode())
                #break

            elif user[0] == "A":
                user_m = user[1].replace("<","").replace(">","").replace("(","").replace(")","").replace(" ","")
                print(user_m)    

                user_m2 = user_m.split(",")

                data_name = pd.read_csv('Name.csv')
                data_age = pd.read_csv('Age.csv')
                data_city = pd.read_csv('City.csv')

                num_n = 0
                num_a = 0
                num_c = 0

                if(len(data_name.index)==0):
                    num_n = 0
                    num_a = 0
                    num_c = 0

                if(len(data_name.index)>0):
                    num_n = data_name['Num'].max()+1
                    num_a = data_age['Num'].max()+1
                    num_c = data_city['Num'].max()+1

                data_name = data_name.append({'Key' : user_m2[0], 'Name' : user_m2[1], 'Num' : num_n}, ignore_index=True)
                data_name = data_name.to_csv('Name.csv', index=False)

                data_age = data_age.append({'Key' : user_m2[0], 'Age' : user_m2[2], 'Num' : num_a}, ignore_index=True)
                data_age = data_age.to_csv('Age.csv', index=False)

                data_city = data_city.append({'Key' : user_m2[0], 'City' : user_m2[3], 'Num' : num_c}, ignore_index=True)
                data_city = data_city.to_csv('City.csv', index=False)


            elif user[0] == "D":
                user_m = user[1].replace("[","").replace("]","").replace(" ","")
                print(user_m)
                #user_m2 = user_m.split(",")

                data_name = pd.read_csv('Name.csv')
                data_age = pd.read_csv('Age.csv')
                data_city = pd.read_csv('City.csv')
                                
                condicion_n=data_name[data_name["Num"]==int(user_m)].index
                data_name = data_name.drop(condicion_n)
                data_name = data_name.to_csv('Name.csv', index=False)

                condicion_a=data_age[data_age["Num"]==int(user_m)].index
                data_age = data_age.drop(condicion_a)
                data_age = data_age.to_csv('Age.csv', index=False)

                condicion_c=data_city[data_city["Num"]==int(user_m)].index
                data_city = data_city.drop(condicion_c)
                data_city = data_city.to_csv('City.csv', index=False)

            
            elif user[0] == "U":

                user_m = user[1].split("(")[0].replace("[","").replace("]","").replace("(","").replace(")","").replace(",","")
                print(user_m)

                user_m2 = user[1].split("(")[1].replace("(","").replace(")","").replace("[","").replace("]","").split(",")
                print(str(user_m2).replace("[","").replace("]","").replace(" ",""))

                data_name = pd.read_csv('Name.csv')
                data_age = pd.read_csv('Age.csv')
                data_city = pd.read_csv('City.csv')
                                
                condicion_n=data_name[data_name["Num"]==int(user_m)].index
                data_name.loc[condicion_n,"Name"]=user_m2[0]
                data_name = data_name.to_csv('Name.csv', index=False)

                condicion_a=data_age[data_age["Num"]==int(user_m)].index
                data_age.loc[condicion_a,"Age"]=user_m2[1]
                data_age = data_age.to_csv('Age.csv', index=False)

                condicion_c=data_city[data_city["Num"]==int(user_m)].index
                data_city.loc[condicion_c,"City"]=user_m2[2]
                data_city = data_city.to_csv('City.csv', index=False)

                                
            elif user[0] == "B":
                
                user_m = user[1].replace("<","").replace(">","").replace(" ","")
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

                                self.wfile.write((f"[{data_name['Num'][i]}]    <{data_name['Key'][i]},({data_name['Name'][i]},{data_age['Age'][j]},{data_city['City'][k]})>\n").encode())


            elif user[0] == "C":

                user_m = user[1].replace("<","").replace(">","").replace(" ","")
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

                                self.wfile.write((f"<{data_name['Key'][i]},({data_name['Name'][i]},{data_age['Age'][j]},{data_city['City'][k]})>\n").encode())


            elif user[0] == "M":
                
                user_m = user[1].replace("<","").replace(">","").replace(" ","")
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

                                self.wfile.write((f"[{data_name['Num'][i]}]    <{data_name['Key'][i]},({data_name['Name'][i]},{data_age['Age'][j]},{data_city['City'][k]})>\n").encode())

        except (SyntaxError):
            self.wfile.write("SyntaxError".encode())
        except (NameError):
            self.wfile.write("NameError".encode())


def main():

    PORT = 8007
    server = HTTPServer(('', PORT), Servidor)
    print("Servidor corriendo en el puerto", PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()
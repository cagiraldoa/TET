from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import pandas as pd
import constants

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(self.path[1:].encode(constants.ENCONDING_FORMAT))

        user = str(self.path[1:]).split("/")
        print (user)
        
        #2self.wfile.write(command)
        
        try:      
            if user[0] == "X" or user[0] == "x":
                self.wfile.write("X".encode(constants.ENCONDING_FORMAT))
                #break

            elif user[0] == "A" or user[0] == "a":
                user_m = user[1].replace("<","").replace(">","").replace(" ","").replace(",+",",")
                print(user_m)    

                user_m2 = user_m.split(",")
                user_m3 = user_m2[1].split("+")

                _1 = pd.read_csv('1.csv')
                _2 = pd.read_csv('2.csv')
                _3 = pd.read_csv('3.csv')
                _4 = pd.read_csv('4.csv')
                _5 = pd.read_csv('5.csv')
                _6 = pd.read_csv('6.csv')
                _7 = pd.read_csv('7.csv')
                _8 = pd.read_csv('8.csv')
                _9 = pd.read_csv('9.csv')
                _10 = pd.read_csv('10.csv')

                num_n = 0


                if(len(_1.index)==0):
                    num_n = 0
 

                if(len(_1.index)>0):
                    num_n = _1['Num'].max()+1



                for i in range(10):
                    if(len(user_m3)<=i):
                        user_m3.append("")

                    if (len(user_m3[i])>0):
                        user_m3[i] = user_m3[i]+" "
                    #print(user_m3[i],i)



                _1 = _1.append({'Key' : user_m2[0], 'Word' : user_m3[0], 'Num' : num_n}, ignore_index=True)
                _1 = _1.to_csv('1.csv', index=False)

                _2 = _2.append({'Key' : user_m2[0], 'Word' : user_m3[1], 'Num' : num_n}, ignore_index=True)
                _2 = _2.to_csv('2.csv', index=False)

                _3 = _3.append({'Key' : user_m2[0], 'Word' : user_m3[2], 'Num' : num_n}, ignore_index=True)
                _3 = _3.to_csv('3.csv', index=False)

                _4 = _4.append({'Key' : user_m2[0], 'Word' : user_m3[3], 'Num' : num_n}, ignore_index=True)
                _4 = _4.to_csv('4.csv', index=False)

                _5 = _5.append({'Key' : user_m2[0], 'Word' : user_m3[4], 'Num' : num_n}, ignore_index=True)
                _5 = _5.to_csv('5.csv', index=False)

                _6 = _6.append({'Key' : user_m2[0], 'Word' : user_m3[5], 'Num' : num_n}, ignore_index=True)
                _6 = _6.to_csv('6.csv', index=False)

                _7 = _7.append({'Key' : user_m2[0], 'Word' : user_m3[6], 'Num' : num_n}, ignore_index=True)
                _7 = _7.to_csv('7.csv', index=False)

                _8 = _8.append({'Key' : user_m2[0], 'Word' : user_m3[7], 'Num' : num_n}, ignore_index=True)
                _8 = _8.to_csv('8.csv', index=False)

                _9 = _9.append({'Key' : user_m2[0], 'Word' : user_m3[8], 'Num' : num_n}, ignore_index=True)
                _9 = _9.to_csv('9.csv', index=False)

                _10 = _10.append({'Key' : user_m2[0], 'Word' : user_m3[9], 'Num' : num_n}, ignore_index=True)
                _10 = _10.to_csv('10.csv', index=False)



            elif user[0] == "D":
                user_m = user[1].replace("[","").replace("]","").replace(" ","")
                print(user_m)
                #user_m2 = user_m.split(",")

                _1 = pd.read_csv('1.csv')
                _2 = pd.read_csv('2.csv')
                _3 = pd.read_csv('3.csv')
                _4 = pd.read_csv('4.csv')
                _5 = pd.read_csv('5.csv')
                _6 = pd.read_csv('6.csv')
                _7 = pd.read_csv('7.csv')
                _8 = pd.read_csv('8.csv')
                _9 = pd.read_csv('9.csv')
                _10 = pd.read_csv('10.csv')
                                
                condicion=_1[_1["Num"]==int(user_m)].index
                
                _1 = _1.drop(condicion)
                _2 = _2.drop(condicion)
                _3 = _3.drop(condicion)
                _4 = _4.drop(condicion)
                _5 = _5.drop(condicion)
                _6 = _6.drop(condicion)
                _7 = _7.drop(condicion)
                _8 = _8.drop(condicion)
                _9 = _9.drop(condicion)
                _10 = _10.drop(condicion)
                
                _1 = _1.to_csv('1.csv', index=False)
                _2 = _2.to_csv('2.csv', index=False)
                _3 = _3.to_csv('3.csv', index=False)
                _4 = _4.to_csv('4.csv', index=False)
                _5 = _5.to_csv('5.csv', index=False)
                _6 = _6.to_csv('6.csv', index=False)
                _7 = _7.to_csv('7.csv', index=False)
                _8 = _8.to_csv('8.csv', index=False)
                _9 = _9.to_csv('9.csv', index=False)
                _10 = _10.to_csv('10.csv', index=False)



            elif user[0] == "U":

                user_m = user[1].split("+(")[0].replace("[","").replace("]","").replace("(","").replace(")","").replace(",","")
                print(user_m)

                user_m2 = user[1].split("+(")[1].replace("(","").replace(")","").replace("[","").replace("]","").replace("\'","").replace(",+",",").split("+")
                print(user[1].split("+(")[1].replace("(","").replace(")","").replace("[","").replace("]","").replace("\'","").replace(",+",","))

                _1 = pd.read_csv('1.csv')
                _2 = pd.read_csv('2.csv')
                _3 = pd.read_csv('3.csv')
                _4 = pd.read_csv('4.csv')
                _5 = pd.read_csv('5.csv')
                _6 = pd.read_csv('6.csv')
                _7 = pd.read_csv('7.csv')
                _8 = pd.read_csv('8.csv')
                _9 = pd.read_csv('9.csv')
                _10 = pd.read_csv('10.csv')


                for i in range(10):
                    if(len(user_m2)<=i):
                        user_m2.append("")

                    if (len(user_m2[i])>0):
                        user_m2[i] = user_m2[i]+" "
                    #print(user_m2[i],i)
                                
                condicion=_1[_1["Num"]==int(user_m)].index
                
                _1.loc[condicion,"Word"]=user_m2[0]
                _2.loc[condicion,"Word"]=user_m2[1]
                _3.loc[condicion,"Word"]=user_m2[2]
                _4.loc[condicion,"Word"]=user_m2[3]
                _5.loc[condicion,"Word"]=user_m2[4]
                _6.loc[condicion,"Word"]=user_m2[5]
                _7.loc[condicion,"Word"]=user_m2[6]
                _8.loc[condicion,"Word"]=user_m2[7]
                _9.loc[condicion,"Word"]=user_m2[8]
                _10.loc[condicion,"Word"]=user_m2[9]


                _1 = _1.to_csv('1.csv', index=False)
                _2 = _2.to_csv('2.csv', index=False)
                _3 = _3.to_csv('3.csv', index=False)
                _4 = _4.to_csv('4.csv', index=False)
                _5 = _5.to_csv('5.csv', index=False)
                _6 = _6.to_csv('6.csv', index=False)
                _7 = _7.to_csv('7.csv', index=False)
                _8 = _8.to_csv('8.csv', index=False)
                _9 = _9.to_csv('9.csv', index=False)
                _10 = _10.to_csv('10.csv', index=False)

                                
            elif user[0] == "B" or user[0] == "b":
                
                user_m = user[1].replace("<","").replace(">","").replace(" ","")
                print(user_m)
                #user_m2 = user_m.split(",")

                _1 = pd.read_csv('1.csv').fillna("")
                _2 = pd.read_csv('2.csv').fillna("")
                _3 = pd.read_csv('3.csv').fillna("")
                _4 = pd.read_csv('4.csv').fillna("")
                _5 = pd.read_csv('5.csv').fillna("")
                _6 = pd.read_csv('6.csv').fillna("")
                _7 = pd.read_csv('7.csv').fillna("")
                _8 = pd.read_csv('8.csv').fillna("")
                _9 = pd.read_csv('9.csv').fillna("")
                _10 = pd.read_csv('10.csv').fillna("")


                for a in _1.index:

                    if(_1['Key'][a]==user_m and _1['Key'][a]==_2['Key'][a]
                    and _1['Key'][a]==_3['Key'][a] and _1['Key'][a]==_4['Key'][a]
                    and _1['Key'][a]==_5['Key'][a] and _1['Key'][a]==_6['Key'][a]
                    and _1['Key'][a]==_7['Key'][a] and _1['Key'][a]==_8['Key'][a]
                    and _1['Key'][a]==_9['Key'][a] and _1['Key'][a]==_10['Key'][a]
                    and _1['Num'][a]==_2['Num'][a]
                    and _1['Num'][a]==_3['Num'][a] and _1['Num'][a]==_4['Num'][a]
                    and _1['Num'][a]==_5['Num'][a] and _1['Num'][a]==_6['Num'][a]
                    and _1['Num'][a]==_7['Num'][a] and _1['Num'][a]==_8['Num'][a]
                    and _1['Num'][a]==_9['Num'][a] and _1['Num'][a]==_10['Num'][a]):

                        self.wfile.write((f"[{_1['Num'][a]}]    < {_1['Key'][a]}, {_1['Word'][a]}{_2['Word'][a]}{_3['Word'][a]}{_4['Word'][a]}{_5['Word'][a]}{_6['Word'][a]}{_7['Word'][a]}{_8['Word'][a]}{_9['Word'][a]}{_10['Word'][a]}>\n").encode(constants.ENCONDING_FORMAT))

                                                        

            elif user[0] == "C" or user[0] == "c":

                user_m = user[1].replace("<","").replace(">","").replace(" ","")
                print(user_m)
                #user_m2 = user_m.split(",")

                _1 = pd.read_csv('1.csv').fillna("")
                _2 = pd.read_csv('2.csv').fillna("")
                _3 = pd.read_csv('3.csv').fillna("")
                _4 = pd.read_csv('4.csv').fillna("")
                _5 = pd.read_csv('5.csv').fillna("")
                _6 = pd.read_csv('6.csv').fillna("")
                _7 = pd.read_csv('7.csv').fillna("")
                _8 = pd.read_csv('8.csv').fillna("")
                _9 = pd.read_csv('9.csv').fillna("")
                _10 = pd.read_csv('10.csv').fillna("")


                for a in _1.index:

                    if(_1['Key'][a]==user_m and _1['Key'][a]==_2['Key'][a]
                    and _1['Key'][a]==_3['Key'][a] and _1['Key'][a]==_4['Key'][a]
                    and _1['Key'][a]==_5['Key'][a] and _1['Key'][a]==_6['Key'][a]
                    and _1['Key'][a]==_7['Key'][a] and _1['Key'][a]==_8['Key'][a]
                    and _1['Key'][a]==_9['Key'][a] and _1['Key'][a]==_10['Key'][a]
                    and _1['Num'][a]==_2['Num'][a]
                    and _1['Num'][a]==_3['Num'][a] and _1['Num'][a]==_4['Num'][a]
                    and _1['Num'][a]==_5['Num'][a] and _1['Num'][a]==_6['Num'][a]
                    and _1['Num'][a]==_7['Num'][a] and _1['Num'][a]==_8['Num'][a]
                    and _1['Num'][a]==_9['Num'][a] and _1['Num'][a]==_10['Num'][a]):

                        self.wfile.write((f"< {_1['Key'][a]}, {_1['Word'][a]}{_2['Word'][a]}{_3['Word'][a]}{_4['Word'][a]}{_5['Word'][a]}{_6['Word'][a]}{_7['Word'][a]}{_8['Word'][a]}{_9['Word'][a]}{_10['Word'][a]}>\n").encode(constants.ENCONDING_FORMAT))

            elif user[0] == "M" or user[0] == "m":
                
                user_m = user[1].replace("<","").replace(">","").replace(" ","")
                print(user_m)
                #user_m2 = user_m.split(",")

                _1 = pd.read_csv('1.csv').fillna("")
                _2 = pd.read_csv('2.csv').fillna("")
                _3 = pd.read_csv('3.csv').fillna("")
                _4 = pd.read_csv('4.csv').fillna("")
                _5 = pd.read_csv('5.csv').fillna("")
                _6 = pd.read_csv('6.csv').fillna("")
                _7 = pd.read_csv('7.csv').fillna("")
                _8 = pd.read_csv('8.csv').fillna("")
                _9 = pd.read_csv('9.csv').fillna("")
                _10 = pd.read_csv('10.csv').fillna("")


                for a in _1.index:

                    if(_1['Key'][a]==user_m and _1['Key'][a]==_2['Key'][a]
                    and _1['Key'][a]==_3['Key'][a] and _1['Key'][a]==_4['Key'][a]
                    and _1['Key'][a]==_5['Key'][a] and _1['Key'][a]==_6['Key'][a]
                    and _1['Key'][a]==_7['Key'][a] and _1['Key'][a]==_8['Key'][a]
                    and _1['Key'][a]==_9['Key'][a] and _1['Key'][a]==_10['Key'][a]
                    and _1['Num'][a]==_2['Num'][a]
                    and _1['Num'][a]==_3['Num'][a] and _1['Num'][a]==_4['Num'][a]
                    and _1['Num'][a]==_5['Num'][a] and _1['Num'][a]==_6['Num'][a]
                    and _1['Num'][a]==_7['Num'][a] and _1['Num'][a]==_8['Num'][a]
                    and _1['Num'][a]==_9['Num'][a] and _1['Num'][a]==_10['Num'][a]):

                        self.wfile.write((f"[{_1['Num'][a]}]    < {_1['Key'][a]}, {_1['Word'][a]}{_2['Word'][a]}{_3['Word'][a]}{_4['Word'][a]}{_5['Word'][a]}{_6['Word'][a]}{_7['Word'][a]}{_8['Word'][a]}{_9['Word'][a]}{_10['Word'][a]}>\n").encode(constants.ENCONDING_FORMAT))



        except (SyntaxError):
            self.wfile.write("SyntaxError".encode(constants.ENCONDING_FORMAT))
        except (NameError):
            self.wfile.write("NameError".encode(constants.ENCONDING_FORMAT))
        except:
            self.wfile.write("\nNo se logro. Error tuyo. Intentalo de nuevo. Pero ahora hazlo bien\n".encode(constants.ENCONDING_FORMAT))


def main():

    server = HTTPServer(('', constants.PORT), Servidor)
    print("Servidor corriendo en el puerto", constants.PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()
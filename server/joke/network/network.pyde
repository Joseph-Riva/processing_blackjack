add_library('net')
myClient = None
        
def load():
    global myClients
    myClients.append(Client(this, "localhost", 5000))
    myClients[-1].write("GET / HTTP/1.1\r\n")
    myClients[-1].write("\r\n")
    if(myClients[0].available() > 0):
        dataIn = myClients[0].readString()
        if('[]' not in dataIn):
            try:
                value = dataIn[dataIn.index('[') + 1:-1]
            except:
                pass
            print(value)
        myClients.pop(0)

def setup():
    global myClients
    myClients = []

def draw():
    load()

add_library('net')
myClient = None
        
def load():
    global myClient
    if(myClient.available() > 0):
        dataIn = myClient.readString()
        print(dataIn)
            
def setup():
    global myClient
    myClient = Client(this, "localhost", 5000)
    myClient.write("GET / HTTP/1.1\r\n")
    myClient.write("\r\n")
    #size(1000,1000)
    load()
    
def draw():
    #myClient.write("GET / HTTP/1.1\r\n")
    load()

add_library('net')
myClient = None
def setup():
    global myClient
    print("12")
    myClient = Client(this, "127.0.0.1", 5000)
    myClient.write("GET / HTTP/1.0\r\n")
    print("hi")
def draw():
    global myClient
    if(myClient.available > 0):
        dataIn = myClient.read()
    print(dataIn)

import socket



def connect():
    print ("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        print ("Connection sucessful")
    except:
        print ("Connection unsucessful. Make sure the server is online.")


def upload(file_name):
    print (f'\nUploading file: {file_name}...')
    s.send(file_name.split("/")[-1].encode())

    with open(file_name, "rb") as f:
        my_file = f.read(BUFFER_SIZE)
        while True:
            s.send(my_file)
            my_file  = f.read(1024)
            if not my_file:
                print("the file is upload")
                break
"""
            #x = (file_name.split("/")[-1].encode())
            #my_file = f"{x}@{my_file}"
            print (my_file)
    except:
        print ("Couldn't open file. Make sure the file name was entered correctly.")
        return
    ""'
    try:
        #s.send(file_name.split("/")[-1].encode())
        #s.send('@'.encode())
        s.send(my_file)
        #print (s.send(my_file))
    except:
        print ("Couldn't make server request. Make sure a connection has bene established.")
        return
    try:
        s.recv(BUFFER_SIZE)
    except:
        print ("Error sending file details")
    return
    """

def exit():
	s.close()


def main():
    print ('\nWelcome')
    connect()
    print ('Choose one of the following options:\n\nSend_file\nexit')
    while True:
        print ('\nenter a command')
        inp = input()
        if inp == 'Send_file':
            upload(input('Enter the file name\n'))
        elif inp == 'exit':
            exit()
            break
        else:
            print('Command not recognised; please try again')
			
    

if __name__=="__main__":
    
    TCP_IP = input('Enter the name IP\n') #"127.0.0.1" # Only a local server
    TCP_PORT = 12345 # Just a random choice
    BUFFER_SIZE = 1024 # Standard chioce
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    main()

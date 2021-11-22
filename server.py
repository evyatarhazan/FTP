import socket


def main():
    soc = socket.socket()
    soc.bind(('', 12345))
    soc.listen(1)
    rsoc, addr = soc.accept()

    

    while True:
        print(rsoc.recv(1024))
        with open('file_name', "ab") as file:
            file.write(rsoc.recv(1024))



if __name__=="__main__":
    main()

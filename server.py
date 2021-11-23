import socket


def main():
    soc = socket.socket()
    soc.bind(('', 12345))
    soc.listen(1)
    rsoc, addr = soc.accept()

    file_name = rsoc.recv(1024).decode()

    with open(file_name,'ab+') as f:
        print("the file pass")
        
        while True:
            data = rsoc.recv(1024)
            f.write(data)
            print(data)

            if not data:
                print("it's Done")
                break


if __name__=="__main__":
    main()

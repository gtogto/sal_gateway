from bluetooth import *

def receiveMsg():
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(('',PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    advertise_service( server_sock, "BtChat",
            service_id = uuid,
            service_classes = [ uuid, SERIAL_PORT_CLASS ],
            profiles = [ SERIAL_PORT_PROFILE ] )
			    
    print("Waiting for connection : channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print('accepted')
    while True:          
        print("Accepted connection from ", client_info)
        try:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)
            print("send [%s]" % data[::-1])
            client_sock.send(data[::-1])
        except IOError:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print("all done")
            break

        except KeyboardInterrupt:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print("all done")
            break
receiveMsg()

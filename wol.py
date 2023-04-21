import socket, sys

#Brodcast ip address, so that every device on the network can recieve the packet
UDP_IP = "255.255.255.255"
UDP_PORT = 9

def wake_up(MAC_ADDRESS: str):
    Message = create_magic_packet(MAC_ADDRESS)
    #create new socket and set UDP protocol
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #set options and allow brodcast (because we way not know the device IP address)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #send the "magic packet" to brodcast ip with port number 9
    soc.sendto(Message,(UDP_IP, UDP_PORT))
    #close socket
    soc.close()

def create_magic_packet(MAC_ADDRESS) -> bytes:
    #magic packet structure:
    # FF FF FF FF FF FF + 16 * (MAC ADDRESS)
    #create UDP "package" with magic packet structure and remove "-" or ":" from mac address
    Message = bytes.fromhex(6 * 'FF' + 16 * MAC_ADDRESS)
    return Message

if '__main__' == __name__:
    if len(sys.argv) < 2:
        print("Please provide mac address")
        exit()
    MAC = sys.argv[1] #get mac adress from second cli argument
    if len(MAC) < 12:
        raise ValueError("Invalid MAC address format")
    wake_up(MAC)

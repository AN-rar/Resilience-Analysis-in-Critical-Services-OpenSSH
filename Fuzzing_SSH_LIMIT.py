import scapy
import socket

LHOST = "127.0.0.1"
PORT = 22

Cantidad = [100, 500, 1000, 5000, 10000]

for i in Cantidad:
    instancia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    instancia.settimeout(2)

    try:
        instancia.connect((LHOST, PORT))
        Basura = "\x00" * i
        print(f"Enviando {i} Caracteres...")

        instancia.send(Basura.encode())
        instancia.recv(1024)
        instancia.close()

    except Exception as e:
        print(f"[!] El servicio cayo o bloque la conexion en {i} bytes: {e}")
        break

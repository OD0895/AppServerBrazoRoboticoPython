#!/usr/bin/python3
import socket, sys, threading
from control.ControladorServos import Controlador

PORT = 9789 
HOST = "192.168.43.53"

class ServidorWifi(threading.Thread):
        
    def __init__(self, port, host, bufferTe):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {} # current connections
        self.bufferTe = bufferTe
        self.controlador = Controlador()
        self.controlador.puntoInicial()        
        
        try:
            self.server.bind((self.host, self.port))
            nombre_equipo = socket.gethostname()
            direccion_equipo = socket.gethostbyname(nombre_equipo)
            #print(direccion_equipo)
            #print ("--SERVIDOR INICIADO--")    
            self.bufferTe.set_text("--SERVIDOR INICIADO--\n")
        except socket.error:
            #print('Fallo la conexion: %s' % (socket.error))
            self.bufferTe.set_text("FALLO, AL REALIZAR LA CONEXION POR WIFI")
            sys.exit(0)

        self.server.listen(10)
        
    def exit(self):
        self.server.close()

    def run_thread(self, conn, addr):
        try:
            #print('CONECTADO CON: ' + addr[0] + ':' + str(addr[1]))
            self.bufferTe.set_text('CONECTADO CON: ' + addr[0] + ':' + str(addr[1]))
            while True:
                data = conn.recv(1024)
                if data:
                    print(data)
                    canal = int(data[0:1])
                    mov = int(data[2:5])
                    self.controlador.movimientoMotor(canal, mov)
                    #conn.sendall(reply)
                else:
                    #print('SE DESCONECTO CLIENTE: ', addr[0])
                    self.bufferTe.set_text('SE DESCONECTO CLIENTE: '+addr[0])
                    break
        finally:
            conn.close() # Close

    def run(self):
        #print('ESPERANDO CONEXIONES EN EL PUERTO: %s' % (self.port))
        self.bufferTe.set_text('ESPERANDO CONEXIONES EN EL PUERTO: %s' % (self.port))
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.run_thread, args=(conn, addr)).start()

    

#server = ServidorWifi(PORT, HOST)
#server.run()
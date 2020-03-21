#!/usr/bin/python3
import bluetooth, sys, threading
from control.ControladorServos import Controlador

class BluetoothServer(threading.Thread):

    def __init__(self, bufferTe):
        threading.Thread.__init__(self)
        self.bufferTe = bufferTe
        self.server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.controlador = Controlador()
        self.controlador.puntoInicial()
        self.port = 1

        try:
            self.server_sock.bind(("", self.port))
            self.bufferTe.set_text("--SERVIDOR INICIADO--\n")
        except Exception as e:
            self.bufferTe.set_text("FALLO, AL REALIZAR LA CONEXION POR BLUETOOTH")

        self.server_sock.listen(1)

    def exit(self):
    	self.client_sock.close()
    	self.server_sock.close()

    def run_thread(self, client_sock, address):
        try:
            self.bufferTe.set_text("CONECTADO CON: "+ address[0])
            while True:
                data = client_sock.recv(1024)
                if data:
                    print(data)  
                    canal = int(data[0:1])
                    mov = int(data[2:5])
                    self.controlador.movimientoMotor(canal, mov)
                else:
                    self.bufferTe.set_text('SE DESCONECTO CLIENTE: '+ address[0])
                    break
        except:
            self.bufferTe.set_text('SE DESCONECTO CLIENTE: '+ address[0])
        finally:
            client_sock.close()

    def run(self):
        self.bufferTe.set_text('ESPERANDO CLIENTE BLUETOOTH')
        while True:
            client_sock,address = self.server_sock.accept()
            threading.Thread(target=self.run_thread, args=(client_sock, address)).start()
#!/usr/bin/python3
import threading, sys, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from control.SocketServer import ServidorWifi
from control.BluetoothServer import BluetoothServer
import time

PORT = 9999 
HOST = "192.168.49.59"  
            
def hiloWifi(puerto, ip, resultado):
    serverWifi = ServidorWifi(puerto, ip, resultado)
    serverWifi.run()    

def hiloBluet(resultado, c):
    serverBluetooth = BluetoothServer(resultado)
    serverBluetooth.run()      

def evento_conectar(button):
    print("ConectarWifi")
    try:
        hiloW = threading.Thread(target=hiloWifi, args=(int(txtPuerto.get_text()), txtIp.get_text(), resultado), daemon = True)
        hiloW.start()      
    except Exception as e:
        print("FALLO: ",e)

def evento_apagar(button):
    print("Apagado")
    sys.exit(0)

def evento_bluet(button):
    print("ConectarBluetooth")
    try:
        hiloB = threading.Thread(target=hiloBluet, args=(resultado, c), daemon = True)
        hiloB.start()      
    except Exception as e:
        print("FALLO: ",e)

handlers = {
    "onDestroy": Gtk.main_quit,
    "evento_conectar": evento_conectar,
    "evento_apagar": evento_apagar,
    "evento_bluet": evento_bluet
}

builder = Gtk.Builder()
builder.add_from_file("frame.glade")
resultado = builder.get_object("texto_res")
c = 0
txtPuerto = builder.get_object("txtPuerto")
txtPuerto.set_text(str(PORT))
txtIp = builder.get_object("txtIp")
txtIp.set_text(HOST)
resultado.set_text("RESULTADO: ")
builder.connect_signals(handlers)
window = builder.get_object("window1")
window.set_default_size(500, 480)
window.show_all()

Gtk.main()


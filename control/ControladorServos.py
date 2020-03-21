#!/usr/bin/python3
from __future__ import division
# Importando la libreria PCA9685.
import Adafruit_PCA9685
import time

class Controlador():

	def __init__(self):
		super(Controlador, self).__init__()
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(60)
		self.arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,61,60,59,58,57,56,55,54,53,52,51,50,49,
		48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,
		19,18,17,16,15,14]

	def puntoInicial(self):
		self.baseG(37)
		self.hombro(45)
		self.codo(18)
		self.mano(38)
		self.muneca(43)
		self.gripper(25)
	
	def movimientoMotor(self, canal, mov):
		if canal == 0:
			self.baseG(mov)
		elif canal == 1:
			self.hombro(mov)
		elif canal == 2:
			self.codo(mov)
		elif canal == 4:
			self.mano(mov)
		elif canal == 5:
			self.muneca(mov)
		elif canal == 6:
			self.gripper(mov)

	def baseG(self, mov):
		#rango de 15-59
		motor = mov * 10
		self.pwm.set_pwm(0, 0, motor)

	def hombro(self, mov):
		#rango de 30-61
		motor1 = (self.arr[mov+1])*10
		motor2 = (mov*10)
		self.pwm.set_pwm(1, 0, motor1)
		self.pwm.set_pwm(7, 0, motor2)

	def codo(self, mov):
		#rango de 18-50 
		motor = mov * 10
		self.pwm.set_pwm(2, 0, motor)

	def mano(self, mov):
		#rango de 24-48
		motor = mov *10
		self.pwm.set_pwm(4, 0, motor)
	
	def muneca(self, mov):
		#rando de 27-60
		motor = mov *10
		self.pwm.set_pwm(5, 0, motor)
	
	def gripper(self, mov):
		#rango de 25-42
		motor = mov *10
		self.pwm.set_pwm(6, 0, motor)
		
#c =Controlador()
#c.puntoInicial()
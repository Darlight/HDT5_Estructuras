# Universidad del Valle de Guatemala
# Seccion 10
# Mario Perdomo 18029 y Josue Sagastume 18173
# Laboratorio 5 - Simulación de corrida de programas en un sistema operativo de tiempo compartido

import simpy
import random
import math
# Intervalo de cuando se genera cuantos procesos solicita la RAM
intervalo = 10
#El entorno que se encuentre la simulacion
env = simpy.Environment()
#Intentos
#No estoy seguro para que sirve el random.seed, recomiendo ver la fuente ya mencionada. 
intentos = random.seed(RANDOM_SEED)


"""
El resumen del ejercicio es basicamente utilizar un simulador que recibe diferentes datos en un container
RAM. Para ello, se simulara una computadora x cantidad de memorias RAMS, donde recibiren y cantidad de
procesos. Luego, se procesaran en un CPU, donde sera un recurso que solo podra hacer un proceso. Todavia entendiendo esa parte.
Descargue la libreria de math para obtener la desviacion estandar. Debemos sacar un length entre todos los datos que hemos simulado
para obtener un promedio y una desviacion estandar.
"""

#procesos es la cantidad de instrucciones a realizar de 1 a 3
#memoria pues la cantidad de cuanta memoria a la ram de 1 a 10
def computadora(env,procesos,cantidad_memoria):
	#Como es un generador, su ciclo es infinito.
	while True:
		#El container de RAM, tiene una capacida de 100
		#Los parametros estan en ingles porque lo pide el simpy
		RAM = simpy.Container(env, init = 0, capacity = cantidad_memoria)
		#El CPU que solo o, lo cual permite realizar tres
		#instrucciones. Esto debe ser variable, ya que podríamos decir luego que tenemos un procesador más rápido que ejecuta más
		#instrucciones en esa unidad de tiempo.
		CPU = simpy.Resource(env, capacity = procesos)
		procesadores = procesos
		



def nuevo(env,procesos,RAM,CPU,cantidad_memoria,instrucciones,salida):
	for i in range(salida,cantidad_memoria):
		tiempo = (1.0/intervalo)
		memoria_RAM = randint(1,10)
		procesos = randint(1,10)
		tiempo_inicial = env.now()
		yield env.process()
def agregar_Datos(env,ram,cantidad_memoria,procesos):
	yield()


#Esta funcion es imporntante, ya que contiene una partee donde interrupte el proceso. 
def correr(env,ram,cantidad_memoria,procesos):
def leer(env,ram,cantidad_memoria,procesos):
def esperar(env,ram,cantidad_memoria,procesos):
def terminar(env,ram,cantidad_memoria,procesos):





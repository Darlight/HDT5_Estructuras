# Universidad del Valle de Guatemala
# Seccion 10
# Mario Perdomo 18029 y Josue Sagastume 18173
# Laboratorio 5 - Simulación de corrida de programas en un sistema operativo de tiempo compartido

import simpy
import random
import math


"""
El resumen del ejercicio es basicamente utilizar un simulador que recibe diferentes datos en un container
RAM. Para ello, se simulara una computadora x cantidad de memorias RAMS, donde recibiren y cantidad de
procesos. Luego, se procesaran en un CPU, donde sera un recurso que solo podra hacer un proceso. Todavia entendiendo esa parte.
Descargue la libreria de math para obtener la desviacion estandar. Debemos sacar un length entre todos los datos que hemos simulado
para obtener un promedio y una desviacion estandar.
"""

datos = []

#procesos es la cantidad de instrucciones a realizar de 1 a 3
#memoria pues la cantidad de cuanta memoria a la ram de 1 a 10

# Intervalo de cuando se genera cuantos procesos solicita la RAM
intervalo = 10
#El entorno que se encuentre la simulacion
env = simpy.Environment()
promedio = 0
desviacion = 0
#Intentos
#No estoy seguro para que sirve el random.seed, recomiendo ver la fuente ya mencionada. 
random.seed(RANDOM_SEED)
procesos = 3
CPU = simpy.Resource(env, capacity = procesos)
memoria = random.randint(1,10)
instrucciones = random.randint(1,10)
RAM = simpy.Container(env, init = 0, capacity = cantidad_memoria)


#Calcular promedio y desviacion estandar de la lista datos
def nuevo(env,procesos,RAM,CPU,cantidad_memoria,instrucciones,intervalo,tiempo):
	for i in range(procesos):
		#Genera nuevos procesos
		yield env.timeout(ranom.expovariate(1.0/intervalo))
		with RAM.get(cantidad_memoria) as colaDelRam:
			yield colaDelRam
			print("El proceso %s se encontro en el nuevo estado en %s" %(i,env.now))
			print("El proceso %s pide %s de RAM" %(i,cantidad_memoria))
			print(Ram.level, "Cantidad libre de RAM")
			env.process(correr(env,RAM,cantidad_memoria,procesos,CPU,i))

	

#Esta funcion es importante, ya que contiene una partee donde interrupte el proceso. 
def correr(env,ram,cantidad_memoria,procesos,CPU,identidad):
	#Si la cantidad de instrucciones es menor o igual a cero, env.process(terminar)
		yield(env.timeout(1))
		print('El Proceso %s se encuentra en modo listo en  %s' % (identidad, env.now))
        print('El Proceso %s pide el CPU' %(identidad))
        print('El Proceso %s contiene  %s instructions' %(identidad, procesos))
		if (instrucciones <= 0):
			with CPU.request as requ:
				yield requ
				print("El Proceso %s esta corriendo"(identidad))

				intrucciones  = instrucciones - procesos
				yield env.timeout((1/instructions) * instructions)
                    instructions = instructions - instructions
                    print('Process %s is Terminated at %s' %(name, env.now))
                    tiempoPromedio = env.now
                    listCPU.append(env.now)
                    RAM.put(ramProcess) 
				env.process(terminar(env))
			yield env.timeout(1)
		elif:
		#Si la cantidad de instrucces es mayor, (tenes que generar un random (1,2) si te da 1 le das env.process(esperar) si te da 2 le das env.process(leer))
	
		
		


def leer(env,ram,cantidad_memoria,procesos,instrucciones,CPU,incial):
	yield env.timeout(1)

def esperar(env,ram,cantidad_memoria,procesos):
	yield env.timeout(1)

def terminar(env,ram,cantidad_memoria,procesos):
	#Calcular tiempo final / inicial 
	#agregarlo a una lista datos. 
	yield env.timeout(1)




# Universidad del Valle de Guatemala
# Seccion 10
# Mario Perdomo 18029 y Josue Sagastume 18173
# Laboratorio 5 - Simulación de corrida de programas en un sistema operativo de tiempo compartido

import simpy
import random
# Intervalo de cuando se genera cuantos procesos solicita la RAM
intervalo = 10
#El entorno que se encuentre la simulacion
env = simpy.Environment()
#Cantidad de procesos
procesos = random.expovariate(1.0/10)
#El container de RAM, tiene una capacida de 100
RAM = simpy.Container(env, init = 0, capacity = 100)
#El CPU 
CPU = simpy.Resource(env, capacity = 1)
#Intentos
intentos = random.seed(RANDOM_SEED)

def simuladorRAM(env,memoriaRAM,numprocesos,cantidad_memoria):
	


import simpy

import random

from random import seed

random.seed(10)

  

def proceso(env, nombre,  CPU, RAM):

    global tiempoPromedio

    tempRAM = random.randint(1,10)

    instrucciones = random.randint(1,10)

    yield env.timeout(random.expovariate(1.0/1)) #Genera un nuevo proceso

    #RAM ------------------------------

    with RAM.get(tempRAM) as queueForRAM:

        yield queueForRAM

        print('Proceso %s esta en nuevo estado a los %s ut' % (nombre, env.now))

        print('Proceso %s solicito %s de RAM' % (nombre, tempRAM))

        procesoRAM = tempRAM

        print(RAM.level,"RAM disponible")

        #CPU ---------

        yield env.timeout(0.5)

        print('Proceso %s esta en modo Listo a los %s ut' % (nombre, env.now))

        print('Proceso %s solicito al CPU' %(nombre))

        print('Proceso %s tiene %s instrucciones' %(nombre, instrucciones))

        while(instrucciones > 0):

            with CPU.request() as req:

                yield req

                print('Proceso %s esta corriendo ahora' % (nombre))

                if((instrucciones - 3) <= 0): ##change this if wanna change the instructions per Process

                    yield env.timeout((1/instrucciones) * instrucciones)

                    instrucciones = instrucciones - instrucciones

                    print('Proceso %s esta Terminado a los %s ut' %(nombre, env.now))

                    tiempoPromedio = env.now

                    listCPU.append(env.now)

                    RAM.put(procesoRAM) 

                else:

                    yield env.timeout(1)

                    instrucciones = instrucciones - 3 ##change this if wanna change the instructions per Process

                    print('Proceso %s deja el CPU a los %s ut' % (nombre, env.now))

                    io = random.randint(1,2)

                    if io == 1:

                        print('Proceso %s esta en modo Espera' % (nombre))

                        yield env.timeout(1)

                    else:

                        print('Proceso %s esta en modo Listo' % (nombre))

                        print('Proceso %s tiene %s instrucciones restantes' % (nombre, instrucciones ))

def nuevo(env, instrucciones, intervalo, cantidad, computador, inicio):

    for i in range(inicio, cantidad):

        tiempo = random.expovariate(1.0 / intervalo)#Generamos el intervalo

        memoria_RAM = random.randint(1, 10)#Generamos la memoria ram que consume el proceso

        instructions = random.randint(1, 10)#Generamos las instrucciones que consume el proceso

        inicial = env.now

        yield env.process(computador.add(memoria_RAM,intervalo))

        print(computador.ram.level)

        yield env.process(ready(env, instructions, instrucciones, memoria_RAM, computador, 'Proceso %d' % i, inicial))

        

        

#Simpy enviroment 

env = simpy.Environment()

CPU = simpy.Resource(env, capacity=1)

RAM = simpy.Container(env, init=100, capacity=100)

instrucciones = 3 #Cantidad de instrucciones por proceso

listCPU = list()

tiempoPromedio = 0 #Tiempo promedio de tiempo por proceso

cantidadDeProcesos = 25 #Cantidad de procesos



#Nuevos procesos

for i in range(cantidadDeProcesos):

    env.process(proceso(env, i, CPU, RAM))

env.run()

tiempoPromedio = tiempoPromedio / cantidadDeProcesos

print("El tiempo promedio ", tiempoPromedio)

desvest = tiempoPromedio / cantidadDeProcesos
print("Desviacion estandar: ", desvest)


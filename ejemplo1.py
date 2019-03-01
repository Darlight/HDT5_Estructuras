#ejemplo1.py
#Fecha de creacion: 30/04/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: El juego del ahorcado
import simpy

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

def main():
    env = simpy.Environment()
    env.process(car(env))
    env.run(until=15)

if __name__ == '__main__':
    main()
 
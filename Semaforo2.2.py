import multiprocessing
import time 
import random 

semaforo_norte = None
semaforo_sul = None
semaforo_decolagem = None


def init(sn, ss, sd):
    global semaforo_norte
    global semaforo_sul
    global semaforo_decolagem
 

    semaforo_norte = sn
    semaforo_sul = ss
    semaforo_decolagem = sd
  
def decolar(pista, aviao):
    global semaforo_norte
    global semaforo_sul
    global semaforo_decolagem

    with semaforo_decolagem:

        if pista ==0:
            with semaforo_norte:
                manobrar(pista, aviao)
                taxiar(pista, aviao)
                decolagem(pista, aviao)
                afastamento (pista, aviao)

                

        else:
            with semaforo_sul:
                manobrar(pista, aviao)
                taxiar(pista, aviao)
                decolagem(pista, aviao)
                afastamento (pista, aviao)

                

          

def manobrar(pista, aviao):
    time.sleep((random.randint(3, 7))/10)
def taxiar(pista, aviao):
    time.sleep((random.randint(5, 10))/10)
def decolagem(pista, aviao):
    time.sleep((random.randint(6, 8))/10)
def afastamento(pista, aviao):
    time.sleep((random.randint(3, 8))/10)





def main():
    sem_norte = None
    sem_sul = None
    sem_decolagem = None
   

    params: int = [(0,0)]* 12

    for i in range (12):
        params[i] = ((random.randint(0,1)), (i+1))

    with multiprocessing.Manager() as manager:
        sem_norte = manager.Semaphore(1)
        sem_sul = manager.Semaphore(1)
        sem_decolagem = manager.Semaphore(2)
        with multiprocessing.Pool(processes=12, initializer=init, initargs=(sem_norte, sem_sul, sem_decolagem)) as pool:
            pool.starmap(decolar,params)

if __name__ == '__main__':
    main()
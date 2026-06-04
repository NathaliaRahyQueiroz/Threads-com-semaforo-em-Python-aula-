import multiprocessing
import time 
import random 

semaforo_pista = None
semaforo_decolagem = None
norte: int =0
sul: int = 0

def init(sp, sd, n, s):
    global semaforo_pista
    global semaforo_decolagem
    global norte
    global sul 

    semaforo_pista = sp
    semaforo_decolagem = sd
    norte = n
    sul = s

def decolar(pista, aviao):
    global semaforo_pista
    global semaforo_decolagem
    global norte
    global sul 


    with semaforo_pista:
        if pista == 0:
            norte.value +=1
        else:
            sul.value +=1

    with semaforo_decolagem:
        manobrar(pista, aviao)
        taxiar(pista, aviao)
        decolagem(pista, aviao)
        afastamento (pista, aviao)
        if pista == 0:
            norte.value = 0
        else:
            sul.value = 0

          



def manobrar(pista, aviao):
    time.sleep((random.randint(3, 7))/1000)
def taxiar(pista, aviao):
    time.sleep((random.randint(5, 10))/1000)
def decolagem(pista, aviao):
    time.sleep((random.randint(6, 8))/1000)
def afastamento(pista, aviao):
    time.sleep((random.randint(3, 8))/1000)





def main():
    sem_pista = None
    sem_decolagem = None
    p_norte: int = 0
    p_sul: int = 0

    p_norte= multiprocessing.Value('i', 0)
    p_sul= multiprocessing.Value('i', 0)

    params: int = [(0,0)]* 12

    for i in range (12):
        params[i] = ((random.randint(0,1)), (i+1))

    with multiprocessing.Manager() as manager:
        sem_pista = manager.Semaphore(1)
        sem_decolagem = manager.Semaphore(2)
        with multiprocessing.Pool(processes=12, initializer=init, initargs=(sem_pista, sem_decolagem, p_norte, p_sul )) as pool:
            pool.starmap(decolar,params)

if __name__ == '__main__':
    main()
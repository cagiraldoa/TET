#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <semaphore.h>
#define MAX_CLIENTES 20
#define SILLAS 10
void *customer(void *num);
void *barber(void *num);
sem_t waitingRoom;
sem_t barberChair;
sem_t barberPillow;
sem_t seatBelt;
int allDone = 0;
int main(int argc, char *argv[])
{
    pthread_t btid;
    pthread_t tid[MAX_CLIENTES];
    int i, numCustomers, numChairs;
    int Number[MAX_CLIENTES];
    printf("Ingrese el numero de clientes: ");
    scanf("%d", &numCustomers);
    numChairs = SILLAS;
    if (numCustomers > MAX_CLIENTES)
    {
        printf("El numero maximo de clientes es %d.\n", MAX_CLIENTES);
        exit(-1);
    }
    for (i = 0; i < MAX_CLIENTES; i++)
    {
        Number[i] = i;
    }
    sem_init(&waitingRoom, 0, numChairs);
    sem_init(&barberChair, 0, 1);
    sem_init(&barberPillow, 0, 0);
    sem_init(&seatBelt, 0, 0);
    // CREAR
    pthread_create(&btid, NULL, barber, NULL);
    for (i = 0; i < numCustomers; i++)
    {
        pthread_create(&tid[i], NULL, customer, (void *)&Number[i]);
    }
    for (i = 0; i < numCustomers; i++)
    {
        pthread_join(tid[i], NULL);
    }
    allDone = 1;
    sem_post(&barberPillow);
    pthread_join(btid, NULL);
}
void *customer(void *number)
{
    int num = *(int *)number;
    int chairs;
    printf("\n----------------------");
    printf("NUEVO CLIENTE -> [%d]", num + 1);
    printf("------------------------\n");
    printf("El cliente [%d] va a ir a la barberia \n", num + 1);
    sleep(rand() % 3);
    printf("El cliente [%d] llego \n", num + 1);
    if (sem_trywait(&waitingRoom) == -1)
    {
        printf("No es posible entrar, esta lleno, el cliente [%d] se va .\n", num);
        return 0;
    }
    sem_getvalue(&waitingRoom, &chairs);
    printf("CLiente [%d] en sala de espera \n", num + 1);
    printf("-----[%d] SILLAS VACIAS RESTANTES------\n", chairs);
    sem_wait(&barberChair);
    sem_post(&waitingRoom);
    int stade;
    sem_getvalue(&barberPillow, &stade);
    if (stade == 0)
    {
        printf("El cliente [%d] desperto al barbero\n", num + 1);
        sem_post(&barberPillow);
    }
    sem_wait(&seatBelt);
    sem_post(&barberChair);
    printf("Cliente [%d] se va \n", num + 1);
    return 0;
}
void *barber(void *num_)
{
    while (!allDone)
    {
        int chairs;
        int num = rand() % 4;
        sem_getvalue(&waitingRoom, &chairs);
        if (chairs == 10)
        {
            printf("Se durmio el barbero porque no tenia trabajo en su momento\n");
            sem_wait(&barberPillow);
        }
        if (!allDone)
        {
            printf("El barbero esta con la eleccion de corte del cliente\n");
            if (num == 1)
            {
                printf("Cliente escoge corte tipo 1---> 500ms de espera\n");
                sleep(5 / 10);
            }
            else if (num == 2)
            {
                printf("Cliente escoge corte tipo 2---> 1000ms de espera\n");
                sleep(1);
            }
            else if (num == 3)
            {
                printf("Cliente escoge corte tipo 3---> 2000ms de espera\n");
                sleep(2);
            }
            else if (num == 4)
            {
                printf("Cliente escoge corte tipo 4---> 3000ms de espera\n");
                sleep(3);
            }
            sem_post(&seatBelt);
            printf("El barbero ha acabado con el cliente que escogio su corte.\n");
        }
    }
    printf("Fin del dia. El barbero se va\n");
    return 0;
}
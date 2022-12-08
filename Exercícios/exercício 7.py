# A minha resolução fica alterando de contador conforme o mesmo termina

from time import sleep

while True:

    # contagem sentido crescente

    for v in range(1, 11):
        print(v)
        sleep(0.5)

        if v == 10:
            print()

            # contagem sentido decrescente

            for n in range(10, 0, -1):
                print(n)
                sleep(0.5)

                if n == 1:
                    print()

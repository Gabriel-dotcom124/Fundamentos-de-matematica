**Vetorização**

*   **Exemplo:** para 1 cliente

#    **Vetorização**
"""

montante = 1000
montante_final = 1001.5

ipca = 0.25 / 100
montante_ipca = montante * (1 + ipca)

print(montante_ipca)

print(montante_final < montante_ipca)

"""

*   **Exemplo:** para 100 mil clientes


"""

from random import random, randint

montante_lista = [randint(0, 5000) for _ in range(0, 100000)]
montante_final_lista = [round(montante * (1 + (0.3 * random() / 100)), 2) for montante in montante_lista]

print(montante_lista[0 : 5])
print(montante_final_lista[0 : 5])

"""

*   **Exemplo:** Usando laço de repetição


"""

from time import time

perdeu = list()

inicio = time()

for montante, montante_final in zip(montante_lista, montante_final_lista):
  perdeu.append(montante_final - montante * (1 + ipca))
fim = time()

perdeu = list(filter(lambda val: True if val < 0 else False, perdeu))
print(f"{len(perdeu)} clientes perderam para inflação")


tempo_lista = fim - inicio
print(tempo_lista)

"""

#   **Pacote Numpy**


"""

import numpy as np

montante_array = np.array(montante_lista)
montante_final_array = np.array(montante_final_lista)

print(montante_array)
print(montante_final_array)

from time import time

inicio = time()
perdeu = montante_final_array - montante_array * (1 + ipca)
fim = time()

perdeu = list(filter(lambda val: True if val < 0 else False, perdeu))
print(f"{len(perdeu)} clientes perderam para inflação")

tempo_array = fim - inicio
print(tempo_array)

import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

"""#    **Constantes**

*   **Numericos**
"""

np.pi

np.e

"""

*   **Nulo**


"""

np.nan

type(np.nan)

"""

*   **Infinito**


"""

np.inf

type(np.inf)

"""#    **Funções Elementares**

*   **Soma**
"""

a3 = a1 + a2
print(a3)


a3 = a1 - a2
print(a3)

"""

*   **Multiplicação**

"""

a3 = a1 * a2
print(a3)


a3 = a1 / a2
print(a3)

"""

*  Exponencial

"""

a3 = a1 ** 2
print(a3)

a3 = np.exp(a1)
print(a3)

a3 = np.sqrt(a1)
print(a3)

"""

*   **Logaritimo**


"""

a3 = np.log(a1)
print(a3)

"""

*   **Trigonometria**


"""

a3 = np.sin(a1)
print(a3)


a3 = np.tan(a1)
print(a3)

"""

#    **Álgebra Vetorial**


"""

a1 = np.array([1, 2, 3])
a2 = np.array([3, 4, 5])

a3 = np.dot(a1, a2)
print(a3)
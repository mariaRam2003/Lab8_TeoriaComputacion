import time
import matplotlib.pyplot as plt

# Funcion del ejercicio
def my_function(n):
    counter = 0
    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

# Lista de tamaños de entrada
input_sizes = [1, 10, 100, 1000, 10000] #No mas de 10000 para que no se tarde tanto

# Medir el tiempo de ejecución para cada tamaño de entrada
execution_times = []
for size in input_sizes:
    start_time = time.time()
    result = my_function(size)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Imprimir resultados en una tablita
print("Tamaño de entrada | Tiempo de ejecución")
print("-" * 40)
for size, time_taken in zip(input_sizes, execution_times):
    print(f"{size:<17} | {time_taken:.6f} segundos")

# Graficar los datos de la tablita
plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Tamaño de entrada vs. Tiempo de ejecución")
plt.grid()
plt.show()


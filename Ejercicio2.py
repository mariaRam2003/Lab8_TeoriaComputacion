import time
import matplotlib.pyplot as plt

def my_function(n):
    if n <= 1:
        return 0  # Devolvemos 0 en lugar de None
    start_time = time.time()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            pass  # Hacer algo insignificante
    end_time = time.time()
    return end_time - start_time

# Lista de tamaños de entrada
input_sizes = [1, 10, 100, 1000, 10000, 100000]

# Medir el tiempo de ejecución para cada tamaño de entrada
execution_times = []
for size in input_sizes:
    execution_time = my_function(size)
    execution_times.append(execution_time)

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

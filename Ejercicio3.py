import cProfile

def function(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            pass  # This is a no-op

if __name__ == "__main__":
    import time

    # Valores de n para evaluar
    n_values = [1, 10, 100, 1000, 10000]

    # Medir el tiempo de ejecución para cada valor de n
    results = []
    for n in n_values:
        start_time = time.time()
        cProfile.run('function({})'.format(n))
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((n, execution_time))

    # Imprimir resultados en una tabla
    print("n\tTiempo de Ejecución (s)")
    for n, time in results:
        print(f"{n}\t{time}")

    # Graficar los resultados
    import matplotlib.pyplot as plt

    n_values, execution_times = zip(*results)
    plt.plot(n_values, execution_times, marker='o')
    plt.xlabel('Tamaño de Input (n)')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tamaño de Input vs. Tiempo de Ejecución')
    plt.show()

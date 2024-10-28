import numpy as np
def seidel_method(A, b, eps, x0):
    n = len(b)
    x = np.copy(x0)
    iterations = 0
    while True:
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        diff = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n)))
        if diff < eps:
            break
        x = x_new
        iterations += 1
    print(f"Решение найдено за {iterations} итераций")
    return x
n = int(input("Введите количество неизвестных: "))
print("Введите матрицу коэффициентов A построчно, разделяя элементы пробелами:")
A = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    A.append(row)
A = np.array(A)
print("Введите вектор свободных членов b (одной строкой, разделяя элементы пробелами):")
b = list(map(float, input().split()))
b = np.array(b)
print("Введите начальное приближение (одной строкой, разделяя элементы пробелами):")
x0 = list(map(float, input().split()))
x0 = np.array(x0)
eps = float(input("Введите точность (например, 0.01): "))
solution = seidel_method(A, b, eps, x0)
if solution is not None:
    print("Решение системы:", solution)
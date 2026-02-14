"""File3. Дано имя файла и вещественные числа A и D. Создать файл вещественных чисел с
данным именем и записать в него 10 первых членов арифметической прогрессии с начальным
членом A и разностью D:
A, A + D, A + 2·D, A + 3·D,..."""
import struct
name = input("Имя БИНАРНОГО файла: ")
A = float(input("A: "))
D = float(input("D: "))

# Создаем бинарный файл
f = open(name, 'wb')
for i in range(10):
    term = A + i * D
    f.write(struct.pack('d', term))  # 'd' = double (8 байт)
f.close()

print(f" Файл '{name}' создан (80 байт)")
with open(name, 'rb') as f:
    data = f.read()
    print(data)
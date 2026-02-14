"""File22. Дан файл вещественных чисел. Создать файл целых чисел, содержащий номера всех
локальных экстремумов исходного файла в порядке убывания (определение локального
экстремума дано в задании File20) """
import struct
# Создаем тестовый бинарный файл
print("Создаю тестовый файл data.bin...")
f = open('data.bin', 'wb')
numbers = [1.0, 3.0, 2.0, 5.0, 1.0, 4.0, 3.0, 2.0, 6.0, 4.0]
for num in numbers:
    f.write(struct.pack('d', num))
f.close()
print(" Создан тестовый data.bin")

# Читаем бинарный файл
f = open('data.bin', 'rb')
nums = []
while True:
    chunk = f.read(8)
    if len(chunk) < 8:
        break
    nums.append(struct.unpack('d', chunk)[0])
f.close()

print(f"  Прочитано {len(nums)} чисел")

# Ищем экстремумы
extr_indices = []
for i in range(1, len(nums) - 1):
    if (nums[i-1] < nums[i] > nums[i+1]) or (nums[i-1] > nums[i] < nums[i+1]):
        extr_indices.append(i + 1)  # +1 для нумерации с 1
with open("data.bin", "rb") as f:
    data = f.read()
    print(data)

extr_indices.sort(reverse=True)

# Записываем в БИНАРНЫЙ файл (как int - 4 байта)
f = open('extr.bin', 'wb')
for idx in extr_indices:
    f.write(struct.pack('i', idx))  # 'i' = int (4 байта)
f.close()

print(f" Найдено {len(extr_indices)} экстремумов")
print(f" Номера записаны в extr.bin")
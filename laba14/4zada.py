"""File50. Даны два файла вещественных чисел с именами S1 и S2, элементы которых упорядочены
по возрастанию. Объединить эти файлы в новый файл с именем S3 так, чтобы его элементы
также оказались упорядоченными по возрастанию """
import struct

# file1.bin
with open('file1.bin', 'wb') as f:
    nums = [1.5, 3.2, 4.7, 8.9, 12.3]
    for x in nums:
        f.write(struct.pack('d', x))

# file2.bin
with open('file2.bin', 'wb') as f:
    nums = [2.1, 5.4, 6.8, 9.0, 11.2, 15.7]
    for x in nums:
        f.write(struct.pack('d', x))


print("file1.bin, file2.bin, созданы")

# 2. Объединяем file1 и file2 в S3.txt (задание File50)
print("\nОбъединяю file1.bin и file2.bin...")

# Читаем file1
nums1 = []
with open('file1.bin', 'rb') as f:
    while True:
        b = f.read(8)
        if len(b) < 8:
            break
        nums1.append(struct.unpack('d', b)[0])

# Читаем file2
nums2 = []
with open('file2.bin', 'rb') as f:
    while True:
        b = f.read(8)
        if len(b) < 8:
            break
        nums2.append(struct.unpack('d', b)[0])

# Объединяем и сортируем
result = nums1 + nums2
result.sort()

# Записываем в S3.txt
with open('S3.txt', 'w') as f:
    for x in result:
        f.write(str(x) + ' ')

print(f"S3.txt создан с {len(result)} числами")

# 3. Создаем архив (как в примере)
print("\nСоздаю архив archive.bin...")

with open('archive.bin', 'wb') as arch:
    # Добавляем file1
    with open('file1.bin', 'rb') as f:
        data = f.read()
        count = len(data) // 8  # количество чисел
        arch.write(struct.pack('i', count))  # размер
        arch.write(data)  # данные

    # Добавляем file2
    with open('file2.bin', 'rb') as f:
        data = f.read()
        count = len(data) // 8
        arch.write(struct.pack('i', count))
        arch.write(data)



print("archive.bin создан")
print("Готово")

with open('file1.bin', 'rb') as f:
    data = f.read()
    print(data)
with open('file2.bin', 'rb') as f:
    data = f.read()
    print(data)

with open ('archive.bin', 'rb') as f:
    data = f.read()
    print(data)
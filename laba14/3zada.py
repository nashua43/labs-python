import struct
# Создаем файл с 60 числами
print("   Создаю файл numbers.bin...")
f = open('numbers.bin', 'wb')
for i in range(1, 61):
    f.write(struct.pack('i', i))
f.close()

# Читаем все числа
print("   Читаю файл numbers.bin...")
f = open('numbers.bin', 'rb')
all_nums = []
while True:
    b = f.read(4)
    if len(b) < 4:
        break
    all_nums.append(struct.unpack('i', b)[0])
f.close()

old_len = len(all_nums)  # СОХРАНЯЕМ старую длину
print(f"   Было чисел: {old_len}")

if old_len > 50:
    all_nums = all_nums[-50:]  # берем последние 50
    print(f"   Удалено первых {old_len - 50} чисел")  # ПРАВИЛЬНО: 60 - 50 = 10

# Записываем обратно
f = open('numbers.bin', 'wb')
for x in all_nums:
    f.write(struct.pack('i', x))
f.close()
print(f"  Оставлено чисел: {len(all_nums)}")
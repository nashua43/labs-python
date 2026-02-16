"""1. Имеется набор геометрических фигур разного цвета. Среди фигур могут встречаться
круги, квадраты и отрезки. Для каждой фигуры известно, какого она цвета. Кроме того, для
круга известен его радиус (тип int), для квадрата – размер стороны (тип int), для отрезка –
длина (тип float). Написать функцию, позволяющую ввести с клавиатуры данные для одной
фигуры. Используя эту функцию, ввести сведения об N фигурах и сохранить их в бинарном
файле. Распечатать на экране содержимое данного файла в виде таблицы."""
import pickle
class Figure:
    def __init__(self, color):
        self.color = color


class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return f"Круг     {self.color}       радиус: {self.radius}"


class Square(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def __str__(self):
        return f"Квадрат  {self.color}       сторона: {self.side}"


class Line(Figure):
    def __init__(self, color, length):
        super().__init__(color)
        self.length = length

    def __str__(self):
        return f"Отрезок  {self.color}       длина: {self.length}"


def input_figure():
    print("\n--- Ввод фигуры ---")

    # Проверка 1: выбор типа
    while True:
        try:
            t = int(
                input("1 - Круг\n2 - Квадрат\n3 - Отрезок\nВыберите тип: "))
            if 1 <= t <= 3:
                break
            print("Ошибка: введите 1, 2 или 3")
        except ValueError:
            print("Ошибка: введите число")

    color = input("Цвет: ")

    # Проверка 2: радиус круга
    if t == 1:
        while True:
            try:
                r = int(input("Радиус: "))
                if r > 0:
                    return Circle(color, r)
                print("Ошибка: радиус должен быть положительным")
            except ValueError:
                print("Ошибка: введите целое число")

    # Проверка 3: сторона квадрата
    elif t == 2:
        while True:
            try:
                s = int(input("Сторона: "))
                if s > 0:
                    return Square(color, s)
                print("Ошибка: сторона должна быть положительной")
            except ValueError:
                print("Ошибка: введите целое число")

    # Проверка 4: длина отрезка
    else:
        while True:
            try:
                l = float(input("Длина: "))
                if l > 0:
                    return Line(color, l)
                print("Ошибка: длина должна быть положительной")
            except ValueError:
                print("Ошибка: введите число")


def save_to_file(figures, filename="figures.dat"): #Сохранение в бинарный файл
    try:  # Проверка 5: сохранение
        with open(filename, 'wb') as f:
            pickle.dump(figures, f)
        print(f"Сохранено в {filename}")
    except:
        print("Ошибка при сохранении")


def load_from_file(filename="figures.dat"): #Загрузка из бинарного файла
    try:  # Проверка 6: загрузка
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except:
        print("Ошибка при загрузке (файл не найден или поврежден)")
        return []


def print_table(figures):
    print("\n" + "=" * 50)
    print("СОДЕРЖИМОЕ ФАЙЛА:")
    print("=" * 50)
    print("Тип      Цвет        Параметр")
    print("-" * 50)
    for fig in figures:
        print(fig)
    print("=" * 50)
    print(f"Всего: {len(figures)} фигур")


def main():
    # Проверка 7: количество фигур
    while True:
        try:
            n = int(input("Сколько фигур ввести? "))
            if n > 0:
                break
            print("Ошибка: введите положительное число")
        except ValueError:
            print("Ошибка: введите целое число")

    figures = []
    for i in range(n):
        print(f"\nФигура {i + 1}:")
        figures.append(input_figure())

    save_to_file(figures)
    print_table(load_from_file())


if __name__ == "__main__":
    main()